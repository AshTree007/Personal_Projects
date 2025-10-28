# File Assistant

A command-line tool to help manage your files by scanning, organizing, and identifying old files.

## Features

*   **Scan Folder:** Lists all files in a specified directory and displays their last modified dates.
*   **Find Old Files:** Identifies files that have not been modified in the last 30 days.
*   **Organize Folder:** Moves files into organized subdirectories based on their file type. The default categories are:
    *   `images`: .png, .jpg, .jpeg
    *   `documents`: .pdf, .docx, .txt
    *   `videos`: .mp4, .mov, .avi

## How to Use

1.  Run the `scheduler.py` script from your terminal:
    ```bash
    python scheduler.py
    ```

2.  You will be presented with a menu of options:
    ```
    === What to Do ===
    1. Scan Folder
    2. Scan for old files
    3. Organize folder
    4. Exit
    ```

3.  Choose an option by entering the corresponding number followed by a space and the path to the folder you want to perform the action on. For example:
    ```
    Choose option followed by a space then the folder to perform action: 1 Documents
    ```
    This will scan the `Documents` folder in your home directory.

## Files

*   `scheduler.py`: The main entry point for the application.
*   `utils/scanner.py`: Contains the function for scanning folders.
*   `utils/old_file.py`: Contains the function for finding old files.
*   `utils/organizer.py`: Contains the function for organizing files.
*   `utils/notif.py`: Contains a function for sending desktop notifications (currently used for macOS).
