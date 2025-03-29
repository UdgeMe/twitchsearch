from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
load_dotenv()
app = FastAPI()

@app.get("/test")
def test():    
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
