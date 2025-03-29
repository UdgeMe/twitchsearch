from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
import os
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

@app.post("/save-game-query/")
def save_game_query(game: GameModel):
    print(game.id)
    print(game.name)
    print(f'https://static-cdn.jtvnw.net/ttv-boxart/{game.id}-600x800.jpg')

@app.get("/search/{query}")
def search(query: str):
    headers = {
        "Client-ID": os.getenv("TWITCH_CLIENT"),
        "Authorization": f"Bearer {get_access_token()}"
    }
    search_game_response = requests.get(f"https://api.twitch.tv/helix/games?name={query}", headers=headers)

    search_game_response_data = search_game_response.json().get("data", [])
    if not search_game_response_data:
        return 'game not found'
    
    game_id = search_game_response_data[0]['id']
    params = {"game_id": game_id, "type": "all"}
    response = requests.get("https://api.twitch.tv/helix/videos", headers=headers, params=params)
    
    return response.json().get("data", [])