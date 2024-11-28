import os
import shutil

def apply_new_structure(organization_plan):
    """Create new directories and move files according to the LLM's proposed structure."""
    for file_info in organization_plan["files"]:
        src = file_info["source_path"]
        dest = file_info["destination_path"]
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)


'''
if __name__ == "__main__":
    # Example organization plan
    organization_plan = {
        "files": [
            {
                "source_path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/moving_test.txt",
                "destination_path": "/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder/test_dir_folder"
            }
        ]
    }

    # Call the apply_new_structure function
    apply_new_structure(organization_plan)
()
'''