import shutil
import os

def organize_file(base_path):
    # List all items in the folder
    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)

        # Only process files, skip folders
        if not os.path.isfile(file_path):
            continue

        # Get file extension safely
        ext = os.path.splitext(filename)[1][1:].lower()

        # Define folder categories
        folders = {
            "images": ["png", "jpg", "jpeg"],
            "documents": ["pdf", "docx", "txt"],
            "videos": ["mp4", "mov", "avi"],
        }

        # Move file if it matches a category
        for folder, extensions in folders.items():
            if ext in extensions:
                dest_folder = os.path.join(base_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, dest_folder)
                print(f"Moved {file_path} -> {dest_folder}")
                break  # Stop checking other categories for this file

