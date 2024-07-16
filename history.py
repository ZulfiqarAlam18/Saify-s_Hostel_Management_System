import main
import db_helper

def history():
    user_input = input("""--------------------------------
    1. Student Data
    2. Employee Data
    3. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        print("Student Data")
        fetch_student_data()
    elif user_input == "2":
        print("Employee Data")
        fetch_employee_data()
    elif user_input == "3":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")

def fetch_student_data():
    print("Fetching student data...")
    query = "SELECT * FROM students"
    students = db_helper.fetch_query(query)
    for student in students:
        print(student)

def fetch_employee_data():
    print("Fetching employee data...")
    query = "SELECT * FROM employees"
    employees = db_helper.fetch_query(query)
    for employee in employees:
        print(employee)
