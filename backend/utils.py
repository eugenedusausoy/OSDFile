import requests
from dotenv import load_dotenv
import os
import json

# Load API key from .env file (if needed)
load_dotenv()
api_key = os.getenv("LLM_API_KEY")  # Not used here but can be included for authentication

def send_to_llm(data):
    """Send a request to the LLM and return the response."""
    url = "http://127.0.0.1:1234/v1/chat/completions"

    # Construct a proper messages payload
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides concise summaries and file organization suggestions."
        },
        {
            "role": "user",
            "content": f"Provide a summary for this file:\n{json.dumps(data, indent=2)}"
        }
    ]

    payload = {
        "model": "llama-3.2-3b-instruct",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 150  # Limit response length
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Print full response for debugging
        print("Full API Response:", response.json())

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

def get_summaries(files_data):
    """Send each file's metadata to the LLM to get content summaries."""
    summaries = {}
    for file_data in files_data:
        try:
            response = send_to_llm(file_data)

            # More robust error and response handling
            if isinstance(response, dict):
                if 'choices' in response and response['choices']:
                    summary = response['choices'][0]['message']['content'].strip()
                    summaries[file_data["name"]] = summary
                elif 'error' in response:
                    summaries[file_data["name"]] = f"Error: {response['error']}"
                else:
                    summaries[file_data["name"]] = "No summary available"
            else:
                summaries[file_data["name"]] = "Unexpected response format"

        except Exception as e:
            print(f"Error processing {file_data['name']}: {e}")
            summaries[file_data["name"]] = f"Error: {str(e)}"

    return summaries

if __name__ == "__main__":
    files_data = [
        # ... your existing files_data list ...
    ]

    # Get and print summaries
    summaries = get_summaries(files_data)
    print("Summaries:", json.dumps(summaries, indent=2))