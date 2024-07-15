import main
def to_do_list():
    user_input = input("""--------------------------------
    1. Add Task
    2. Remove Task
    3. View Tasks
    4. Back to Main Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        remove_task()
    elif user_input == "3":
        view_tasks()
    elif user_input == "4":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")
    
def add_task():
    id = input("Enter task ID(any number like 3344):")
    task = input("Enter task Discription: ")
    date = input("Date:")
    time = input("Time:")
    print(f"Task '{task}' added successfully.")

def remove_task():
    id = input("Enter Task ID to remove: ")
   
def view_tasks():
    print("To-Do List:")
