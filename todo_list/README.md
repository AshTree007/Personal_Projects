# To-Do List Command-Line Application

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This project is a simple command-line interface (CLI) to-do list application that enables users to manage their tasks efficiently. Task data is persistently stored in a local SQLite database.

---

## Features

*   **Add Tasks:** Users can add new tasks to their to-do list.
*   **View Tasks:** Displays all tasks with their current status (completed or pending).
*   **Mark Tasks as Done:** Allows users to mark specific tasks as completed.
*   **Delete Tasks:** Provides functionality to remove tasks from the list.
*   **Persistent Storage:** All tasks are saved in a `todo.db` SQLite database file, ensuring data is retained across application sessions.

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
    cd Personal_projects/todo_list
    ```

### Usage

To operate the to-do list application:

1.  **Run the Application:** From the `todo_list` directory, execute the `main.py` script:
    ```bash
    python main.py
    ```
2.  **Interact with the Menu:** A menu of options will be presented in the terminal:
    ```
    === TO-DO LIST ===
    1. Add task
    2. View tasks
    3. Mark task as done
    4. Delete task
    5. Exit
    ```
3.  **Select an Option:** Enter the number corresponding to the desired action and press Enter. Follow any subsequent prompts.

---

## Project Structure

```
todo_list/
├───README.md
└───main.py
└───todo.db (generated upon first run)
```

---

## Technologies Used

*   Python
*   SQLite3 (built-in Python module)

---