from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
load_dotenv()
app = FastAPI()

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