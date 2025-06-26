import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Task title: ")
            tasks.append({"title": title, "completed": False})
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Task number to complete: ")) - 1
            tasks[idx]["completed"] = True
        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Task number to delete: ")) - 1
            tasks.pop(idx)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")
