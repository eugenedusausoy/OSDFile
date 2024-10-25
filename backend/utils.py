import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("LLM_API_KEY")

def send_to_llm(payload):
    """Send a request to the LLM and return the response."""
    url = "https://api.example.com/llm"
    headers = headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
