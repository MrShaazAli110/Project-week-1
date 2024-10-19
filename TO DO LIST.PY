def display_menu():  #making a Main Memu where we will going to select with task to perform.
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")

def add_task(tasks):  #Opiton to add new task
    task = input("Enter Task Description: ")
    tasks.append(task)
    print("Task added Successsfuly! ")


def view_tasks(tasks): #Viewing the New task's or existing ones.
    print("\nTasks: ")
    for i,task in enumerate(tasks, start=1):
        print(f"{1}. {task}")


def mark_task_done(tasks):  #After the task has been Completed then remove the task's
    if not tasks:
        print("No tasks to mark as done")
        return
    
    view_tasks(tasks)    #display then remove the task!
    index = int(input("Enter task index to mark as done: ")) -1

    if 0 <= index < len(tasks): #for deleting the index  value's and the index values is going to be in only 1 in the value we gotta use name to remove it!
        removed_task = tasks.pop(index)
        print(f"Task'{removed_task}' marked as done and removed. ")
    else:
        print("Invalid task index. ")

def save_tasks(tasks):
    with open("tasks.txt","w") as f:
        for task in tasks:
            f.write(task + '\n')

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            return
        f.read().splitlines()
    except FileNotFoundError:
        return []
    
    

def main():
    tasks = load_tasks() #Initialize an empty list to store tasks


    while True:
        display_menu()

        choice = input("Enter Your Choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
    
