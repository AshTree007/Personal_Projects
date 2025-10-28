# To-Do List

This is a simple command-line to-do list application that allows you to manage your tasks. The tasks are stored in a local SQLite database.

## Features

*   **Add Tasks:** Add new tasks to your to-do list.
*   **View Tasks:** View all the tasks in your to-do list with their status (done or not done).
*   **Mark Tasks as Done:** Mark tasks as completed.
*   **Delete Tasks:** Remove tasks from your to-do list.
*   **Persistent Storage:** Tasks are saved in a `todo.db` SQLite database file, so your data is not lost when you close the application.

## How to Use

1.  Run the `main.py` script from your terminal:
    ```bash
    python main.py
    ```

2.  You will be presented with a menu of options:
    ```
    === TO-DO LIST ===
    1. Add task
    2. View tasks
    3. Mark task as done
    4. Delete task
    5. Exit
    ```

3.  Choose an option by entering the corresponding number.

## Files

*   `main.py`: The main script for the to-do list application.
*   `todo.db`: The SQLite database file where the tasks are stored (this file will be created when you first run the application).
