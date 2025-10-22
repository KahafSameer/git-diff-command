import json
import os

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({'id': len(self.tasks) + 1, 'task': task, 'completed': False})
        self.save_tasks()
        print(f"Task '{task}' added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "[X]" if task['completed'] else "[ ]"
            print(f"{task['id']}. {status} {task['task']}")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{task['task']}' removed.")
                return
        print("Task not found.")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task '{task['task']}' marked as completed.")
                return
        print("Task not found.")

def main():
    todo = TodoList()
    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to remove: "))
                todo.remove_task(task_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_completed(task_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
