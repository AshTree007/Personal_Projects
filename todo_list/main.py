import sqlite3 as sq
from datetime import datetime as dt

db = "todo.db"

def init_db():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              task TEXT NOT NULL,
              done BOOLEAN NOT NULL DEFAULT 0,
              time_added TEXT NOT NULL,
              time_completed TEXT
              )''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sq.connect(db)
    c = conn.cursor()
    now = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO tasks (task,time_added) VALUES (?,?)", (task, now))
    conn.commit()
    conn.close()
    print(f"\nTask: {task} Added at {now}\n ")

def list_tasks():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    print()

    if not tasks:
        print("\nNo tasks found\n")
    
    else:
        for task in tasks:
            status = "✅" if task[2] else "❌"
            print(f"{task[0]} {task[1]} {status} time added: {task[3]}, time completed: {task[4]}")
        print()

def mark_done(task_id):
    conn = sq.connect(db)
    c = conn.cursor()
    now = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("UPDATE tasks SET done = 1, time_completed = ? WHERE id = ?", (now, task_id,))
    if c.rowcount == 0:
        print("\nNo task found with that ID.\n")
    else:
        print(f"\nTask {task_id} marked as done at {now}.\n")
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    c.execute("UPDATE tasks SET id = id - 1 WHERE id > ? ", (task_id,))
    if c.rowcount == 0:
        print("\nNo task found with that ID.\n")
    else:
        print(f"\nTask {task_id} deleted.\n")
    conn.commit()
    conn.close()

def main():
    init_db()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = input("Enter task ID: ").strip()
            mark_done(task_id)
        elif choice == '4':
            task_id = input("Enter task ID: ").strip()
            delete_task(task_id)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
