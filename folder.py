# I used this script to organize the tasks within a folder, with task sheet, and my submision files.

import os
import shutil

# Path to the directory containing the files
directory_path = '.'

# Get a list of all files in the directory
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

for file in files:
    # Extract the file name without the extension
    folder_name = os.path.splitext(file)[0]

    # Create the full path for the new folder
    folder_path = os.path.join(directory_path, folder_name)

    # Create the folder if it doesn't already exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Created folder: {folder_path}')
    else:
        print(f'Folder already exists: {folder_path}')

    # Move the file into the newly created folder
    src_file_path = os.path.join(directory_path, file)
    dest_file_path = os.path.join(folder_path, file)
    shutil.move(src_file_path, dest_file_path)
    print(f'Moved file: {src_file_path} to {dest_file_path}')
