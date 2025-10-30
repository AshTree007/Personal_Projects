# File Assistant

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

A command-line and GUI tool for managing files by scanning, organizing, and identifying old files.

---

## Features

*   **Scan Folder:** Lists all files in a specified directory and displays their last modified dates.
*   **Find Old Files:** Identifies files that have not been modified in the last 30 days.
*   **Organize Folder:** Moves files into organized subdirectories based on their file type. The default categories are:
    *   `images`: .png, .jpg, .jpeg
    *   `documents`: .pdf, .docx, .txt
    *   `videos`: .mp4, .mov, .avi
*   **GUI:** A graphical user interface to perform all the file management tasks.

---

## Getting Started

### Prerequisites

*   Python 3.x

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Personal_projects.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Personal_projects/file_assistant
    ```

### Usage

#### Command-Line Interface (CLI)

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

#### Graphical User Interface (GUI)

1.  Run the `main.py` script from your terminal:
    ```bash
    python main.py
    ```

2.  The GUI will launch, allowing you to select a folder and choose an action to perform.

---

## Project Structure

```
file_assistant/
├───README.md
├───main.py
├───scheduler.py
└───utils/
    ├───__init__.py
    ├───notif.py
    ├───old_file.py
    ├───organizer.py
    └───scanner.py
```

---

## Technologies Used

*   Python

---