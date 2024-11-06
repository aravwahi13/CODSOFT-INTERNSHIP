import pickle
import os

class TodoList:
    def __init__(self, filename='todo_list.pkl'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()
        print(f"Task '{task}' added.")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['task'] = new_task
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                print(f"{i}. {task['task']} [{status}]")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the new task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the updated task: ")
            todo_list.update_task(index, new_task)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
