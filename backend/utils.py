import requests
from dotenv import load_dotenv
import os

# Load API key from .env file (if needed)
load_dotenv()
api_key = os.getenv("LLM_API_KEY")  # Not used here but can be included for authentication

def send_to_llm(messages):
    """Send a request to the LLM and return the response."""
    url = "http://127.0.0.1:1234/v1/chat/completions"  # Adjusted endpoint for a ChatGPT-like API

    payload = {
        "model": "llama-3.2-3b-instruct",  # Replace with your specific model name
        "messages": messages,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}
