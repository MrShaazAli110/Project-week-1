tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i + 1}. {task['name']} - {status}")

def mark_as_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]

while True:
    print("\nTO-DO LIST MENU:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        add_task(task_name)
        print("Task added successfully.")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        mark_as_completed(task_index)
        print("Task marked as completed.")

    elif choice == "4":
        view_tasks()
        task_index = int(input("Enter the task number to remove: ")) - 1
        remove_task(task_index)
        print("Task removed successfully.")

    elif choice == "5":
        print("Goodbye!")
