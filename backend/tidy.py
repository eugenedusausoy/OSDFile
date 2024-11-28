from file_loader import retrieve_file_metadata
from directory_tree_maker import get_summaries, propose_new_structure
from organizer import apply_new_structure

def tidy_folder(directory):
    """Main function to tidy a folder using an LLM."""
    # Step 1: Load file metadata
    files_data = retrieve_file_metadata(directory)

    # Step 2: Get summaries
    summaries = get_summaries(files_data)

    # Keep summaries as a variable in memory
    print("Summaries:", summaries)  # Debug: View summaries if needed

    # Step 3: Propose a new directory structure
    organization_plan = propose_new_structure(summaries)

    # Keep the proposed organization plan in memory
    print("Proposed Organization Plan:", organization_plan)  # Debug: View organization plan if needed

    # Step 4: Apply the new structure
    apply_new_structure(organization_plan)

# Declare the variables at the module level to make them accessible publicly if needed
summaries = None
organization_plan = None

if __name__ == "__main__":
    target_directory = "/path/to/target/directory"  # Set by the user
    tidy_folder(target_directory)
