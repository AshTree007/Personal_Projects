import os
from utils import old_file, organizer,scanner

def main():
    while True:
        print("=== What to Do ===")
        print("1. Scan Folder")
        print("2. Scan for old files")
        print("3. Organize folder")
        print("4. Exit")
        user_input = input("Choose option followed by a space then the folder to perform action: ")
        
        if user_input == "4":
                print("Exited")
                exit()

        choice, folder= user_input.split()

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        
        folder_path = os.path.expanduser(f"~/{folder}")
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder}' not found at {folder_path}")
            continue

        if choice == "1":
            files = scanner.scan_folder(folder_path)
            for file, date in files.items():
                print(f"{file.split("/")[-1]}, Date Modified: {date}")

        if choice == "2":
            old_files = old_file.find_old_files(folder_path)
            print("These files were last modified over 30 days ago")
            for file in old_files:
                print(file.split("/")[-1])

        if choice == "3":
            
            if organizer.organize_file(folder_path):
                print(f"Successfully organized '{folder}'")
            else:
                print(f"No files to organize in '{folder}'")


if __name__ == "__main__":
    main()