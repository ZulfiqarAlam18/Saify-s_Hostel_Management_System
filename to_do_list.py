import main
def to_do_list():
    user_input = input("""--------------------------------
    1. Add Task
    2. Remove Task
    3. View Tasks
    4. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        remove_task()
    elif user_input == "3":
        view_tasks()
    elif user_input == "4":
        print("Getting back to menu...")
        main()
    else:
        print("Invalid choice. Please try again.")
    
def add_task():
    task = input("Enter task: ")
    date = input("Enter task date")
    time = input("Enter task time")
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