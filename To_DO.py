# To-Do List App

# Define Task class
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False  # Tasks start as incomplete by default
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.title} - {status}"

# Define ToDoList class to manage multiple tasks
class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize with an empty task list
    
    def add_task(self, title):
        task = Task(title)  # Create a new task
        self.tasks.append(task)  # Add to the task list
        print(f"Task '{title}' added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    
    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].title}' marked as complete.")
        else:
            print("Invalid task number.")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' removed.")
        else:
            print("Invalid task number.")

# Main interaction
if __name__ == "__main__":
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        
        elif choice == '2':
            todo_list.view_tasks()
        
        elif choice == '3':
            index = int(input("Enter task number to mark complete: ")) - 1
            todo_list.mark_task_complete(index)
        
        elif choice == '4':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        
        elif choice == '5':
            print("Exiting To-Do List App.")
            break
        
        else:
            print("Invalid choice. Please try again.")
