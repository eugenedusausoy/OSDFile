import os

def retrieve_file_metadata(directory):
    """Retrieve file names and metadata from the target directory."""
    files_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            metadata = {
                "name": file,
                "path": file_path,
                "size": os.path.getsize(file_path),
                "modified": os.path.getmtime(file_path)
            }
            files_data.append(metadata)
    return files_data


if __name__ == "__main__":
    files_data = retrieve_file_metadata('/Users/eugenedusausoy/Desktop/Projects for a regular career/AI FOCUS/FM Program/OSDFile/test_folder')
    print(files_data)
