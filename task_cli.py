import sys
import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

# Load tasks from file or create empty list if file doesn't exist
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Generate new task ID
def get_new_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1

# Add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_new_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {new_task["id"]})')

# Update a task description
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found")
    else:
        save_tasks(updated_tasks)
        print("Task deleted successfully")

# Mark task
def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task marked as {status}')
            return
    print("Task not found")

# List tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered = tasks if not filter_status else [t for t in tasks if t["status"] == filter_status]

    if not filtered:
        print("No tasks found.")
        return

    for task in filtered:
        print(f'[{task["id"]}] {task["description"]} - {task["status"]} (created: {task["createdAt"]})')

# Entry point
def main():
    if len(sys.argv) < 2:
        print("No command provided.")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            description = sys.argv[2]
            add_task(description)

        elif command == "update":
            task_id = int(sys.argv[2])
            new_desc = sys.argv[3]
            update_task(task_id, new_desc)

        elif command == "delete":
            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == "mark-in-progress":
            task_id = int(sys.argv[2])
            mark_status(task_id, "in-progress")

        elif command == "mark-done":
            task_id = int(sys.argv[2])
            mark_status(task_id, "done")

        elif command == "list":
            if len(sys.argv) == 3:
                status = sys.argv[2]
                list_tasks(status)
            else:
                list_tasks()

        else:
            print("Unknown command.")

    except IndexError:
        print("Missing arguments.")
    except ValueError:
        print("Invalid ID format.")

if __name__ == "__main__":
    main()
