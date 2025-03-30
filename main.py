from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
import os
import asyncio
load_dotenv()
app = FastAPI()

# Configuration CORS pour autoriser les appels API depuis vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_access_token():
    response = requests.post(
        "https://id.twitch.tv/oauth2/token",
        params={
            "client_id": os.getenv("TWITCH_CLIENT"),
            "client_secret": os.getenv("TWITCH_SECRET"),
            "grant_type": "client_credentials"
        },
    )
    data = response.json()
    return data.get("access_token")

def get_db_connection():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    return client.twitch

@app.get("/search-game/{query}")
def search(query: str):
    headers = {
        "Client-ID": os.getenv("TWITCH_CLIENT"),
        "Authorization": f"Bearer {get_access_token()}"
    }
    search_game_response = requests.get(f"https://api.twitch.tv/helix/games?name={query}", headers=headers)

    search_game_response_data = search_game_response.json().get("data", [])
    
    return search_game_response_data

class GameModel(BaseModel):
    id: int
    name: str

@app.post("/game/")
def add_game(game: GameModel):
    db = get_db_connection()

    if db.games.find_one({"id": game.id}):
        return 'game already in db'

    db.games.insert_one({
        "id": game.id,
        "name": game.name,
    })
    return 'game saved'

@app.delete("/game/{gameId}")
def delete_game(gameId: int):
    db = get_db_connection()

    if db.games.find_one({"id": gameId}) is not None:
        db.games.delete_one({
            "id": gameId,
        })

    return 'game deleted'

@app.get("/my-games/")
def my_games():
    
    db = get_db_connection()
    return [
        {
            'id': game['id'],
            'name': game['name'],
            'img': f'https://static-cdn.jtvnw.net/ttv-boxart/{game['id']}-100x130.jpg'
        }
        for game in db.games.find().sort("name")
    ]

active_connections = []
@app.websocket("/ws/get-videos/{gameId}")
async def websocket_videos(websocket: WebSocket, gameId: str):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            videos = await fetch_videos(gameId)
            await websocket.send_json(videos)
            await asyncio.sleep(120) 
    except WebSocketDisconnect:
        active_connections.remove(websocket)

async def fetch_videos(gameId: str):
    headers = {
        "Client-ID": os.getenv("TWITCH_CLIENT"),
        "Authorization": f"Bearer {get_access_token()}"
    }
    params = {"game_id": gameId, "type": "all"}
    response = requests.get(
        "https://api.twitch.tv/helix/videos",
        headers=headers,
        params=params,
    )
    
    return response.json().get("data", [])