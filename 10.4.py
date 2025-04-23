import os
import shutil

def copy_file_to_new_subdir(source_dir, filename, new_subdir):
    # Create the new subdirectory if it doesn't exist
    if not os.path.exists(new_subdir):
        os.makedirs(new_subdir)
        print(f"Created new subdirectory: {new_subdir}")
    
    # Construct full paths
    source_path = os.path.join(source_dir, filename)
    dest_path = os.path.join(new_subdir, filename)

    # Copy the file
    if os.path.isfile(source_path):
        shutil.copy(source_path, dest_path)
        print(f"Copied '{filename}' from '{source_dir}' to '{new_subdir}'")
    else:
        print(f"File '{filename}' not found in '{source_dir}'.")

# Example usage:
source_directory = 'source_folder'       # Replace with your source directory
file_to_copy = 'example.txt'             # Replace with your file name
destination_subdirectory = 'new_folder'  # Replace with your target subdirectory

copy_file_to_new_subdir(source_directory, file_to_copy, destination_subdirectory)
