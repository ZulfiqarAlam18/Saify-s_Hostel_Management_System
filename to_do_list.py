
def to_do_list():
    user_input = input("Enter choice (Number):\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Back to Menu\n:")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        remove_task()
    elif user_input == "3":
        view_tasks()
    elif user_input == "4":
        print("Getting back to menu...")
        # main()
    else:
        print("Invalid choice. Please try again.")
    
def add_task():
    task = input("Enter task: ")
    to_do_list.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    task = input("Enter task to remove: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(to_do_list, start=1):
        print(f"{i}. {task}")

to_do_list = []