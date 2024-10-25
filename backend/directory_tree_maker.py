# directory_tree_maker.py
import json
from utils import send_to_llm  # Assume this sends data to the LLM and gets a response

def get_summaries(files_data):
    """Send each file's metadata to the LLM to get content summaries."""
    summaries = {}
    for file_data in files_data:
        response = send_to_llm({"file_data": file_data, "task": "summarize"})
        summaries[file_data["name"]] = response["summary"]
    return summaries

def propose_new_structure(summaries):
    """Send summaries to the LLM to propose a new naming and directory structure."""
    response = send_to_llm({"summaries": summaries, "task": "organize"})
    return response  # Contains source paths and proposed destination paths
