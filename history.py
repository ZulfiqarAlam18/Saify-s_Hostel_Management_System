import main
import db_helper

def history():
    user_input = input("""--------------------------------
    1. View Students History
    2. View Employees History
    3. View Finance History
    4. Back to Main Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        view_students_history()
    elif user_input == "2":
        view_employees_history()
    elif user_input == "3":
        view_finance_history()
    elif user_input == "4":
        main.main()
    else:
        print("Invalid choice. Please try again.")
    
def view_students_history():
    try:
        query = "SELECT * FROM students"
        students = db_helper.fetch_query(query)
        for student in students:
            print(student)
    except Exception as e:
        print(f"Error: {e}")

def view_employees_history():
    try:
        query = "SELECT * FROM employees"
        employees = db_helper.fetch_query(query)
        for employee in employees:
            print(employee)
    except Exception as e:
        print(f"Error: {e}")

def view_finance_history():
    try:
        query = "SELECT * FROM finance"
        finance_records = db_helper.fetch_query(query)
        for record in finance_records:
            print(record)
    except Exception as e:
        print(f"Error: {e}")
