import json
from utils import send_to_llm

def get_summaries(files_data):
    """Send each file's metadata to the LLM to get content summaries."""
    summaries = {}
    for file_data in files_data:
        try:
            response = send_to_llm({"file_data": file_data, "task": "summarize"})

            # Extract the summary from the LLM response
            if response and 'choices' in response and response['choices']:
                summary = response['choices'][0]['message']['content']
                summaries[file_data["name"]] = summary
            else:
                summaries[file_data["name"]] = "No summary available"

        except Exception as e:
            print(f"Error processing {file_data['name']}: {e}")
            summaries[file_data["name"]] = f"Error: {str(e)}"

    return summaries

def propose_new_structure(summaries):
    """Send summaries to the LLM to propose a new naming and directory structure."""
    try:
        response = send_to_llm({"summaries": summaries, "task": "Organize these files with an appropriate file structure, according to their contents. You will organize "})

        # Extract the content from the LLM response
        if response and 'choices' in response and response['choices']:
            return response['choices'][0]['message']['content']
        else:
            return "Could not generate new structure"
    except Exception as e:
        print(f"Error in propose_new_structure: {e}")
    return None

if __name__ == "__main__":

    files_data =[
        {
            "name": "moving_test.txt",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/moving_test.txt",
            "size": 146,
            "modified": 1732813649.5821166
        },
        {
            "name": "somatosensory.pdf",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/somatosensory.pdf",
            "size": 145349,
            "modified": 1732479983.6672962
        },
        {
            "name": "5538262-hd_1920_1080_25fps.mp4",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/5538262-hd_1920_1080_25fps.mp4",
            "size": 9608839,
            "modified": 1732480204.0546973
        },
        {
            "name": "IBAN",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/IBAN",
            "size": 151,
            "modified": 1732479715.3657424
        },
        {
            "name": "DUSAUSOY_Eugene_ENG_FR_compressed.pdf",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/DUSAUSOY_Eugene_ENG_FR_compressed.pdf",
            "size": 85510,
            "modified": 1732404533.0
        },
        {
            "name": "closeup-of-cactus-full-frame.webp",
            "path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/closeup-of-cactus-full-frame.webp",
            "size": 98992,
            "modified": 1732480092.806227
        }
    ]

    propose_new_structure(get_summaries(files_data))