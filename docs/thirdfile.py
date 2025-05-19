import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                 )''')
    conn.commit()
    return conn

def add_task(conn):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    if not title:
        print("Title is required.")
        return
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
                 (title, description, "Pending", created_at))
    conn.commit()
    print("Task added.")

def view_tasks(conn, filter_status=None):
    cursor = conn.cursor()
    if filter_status:
        cursor.execute("SELECT * FROM tasks WHERE status = ? ORDER BY created_at", (filter_status,))
    else:
        cursor.execute("SELECT * FROM tasks ORDER BY created_at")
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found.")
    else:
        for row in rows:
            print(f"\nID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Description: {row[2]}")
            print(f"Status: {row[3]}")
            print(f"Created At: {row[4]}")

def mark_complete(conn):
    try:
        task_id = int(input("Enter task ID to mark complete: "))
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        if cur.fetchone():
            conn.execute("UPDATE tasks SET status = ? WHERE id = ?", ("Completed", task_id))
            conn.commit()
            print("Task marked as completed.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID.")

def delete_task(conn):
    try:
        task_id = int(input("Enter task ID to delete: "))
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        if cur.fetchone():
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            print("Task deleted.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID.")

def task_menu():
    print("\n=== Task Manager ===")
    print("1. View All Tasks")
    print("2. View Pending Tasks")
    print("3. View Completed Tasks")
    print("4. Add Task")
    print("5. Mark Task as Completed")
    print("6. Delete Task")
    print("7. Exit")

def main():
    conn = connect_db()
    while True:
        task_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            view_tasks(conn)
        elif choice == '2':
            view_tasks(conn, "Pending")
        elif choice == '3':
            view_tasks(conn, "Completed")
        elif choice == '4':
            add_task(conn)
        elif choice == '5':
            mark_complete(conn)
        elif choice == '6':
            delete_task(conn)
        elif choice == '7':
            conn.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
