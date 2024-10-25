import requests

def send_to_llm(payload):
    """Send a request to the LLM and return the response."""
    url = "https://api.example.com/llm"
    headers = {"Authorization": "Bearer API_KEY"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
