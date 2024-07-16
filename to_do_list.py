import main
from db_helper import connect_db

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
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_task():
    task_id = input("Enter Task ID:")
    task_description = input("Enter Task Description:")
    date = input("Enter Date (YYYY-MM-DD):")
    time = input("Enter Time (HH:MM):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO tasks (task_id, task_description, date, time)
        VALUES (?, ?, ?, ?)
        ''', (task_id, task_description, date, time))
        conn.commit()
        conn.close()
        print("Task added successfully.")
    except Exception as e:
        print("An error occurred while adding task:", str(e))

def remove_task():
    task_id = input("Enter Task ID to remove:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM tasks WHERE task_id = ?
        ''', (task_id,))
        conn.commit()
        conn.close()
        print("Task removed successfully.")
    except Exception as e:
        print("An error occurred while removing task:", str(e))

def view_tasks():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM tasks
        ''')
        tasks = cursor.fetchall()
        conn.close()

        print("To-Do List:")
        for task in tasks:
            print(task)
    except Exception as e:
        print("An error occurred while fetching tasks:", str(e))
