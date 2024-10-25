import os
import shutil

def apply_new_structure(organization_plan):
    """Create new directories and move files according to the LLM's proposed structure."""
    for file_info in organization_plan["files"]:
        src = file_info["source_path"]
        dest = file_info["destination_path"]
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)
