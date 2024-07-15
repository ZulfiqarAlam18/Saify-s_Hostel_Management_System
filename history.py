import main
def history():
    user_input = input("""--------------------------------
    1.Student Data
    2.Employee Data
    3. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        print("Student Data")
        # fetch_student_data()
    elif user_input == "2":
        print("Employee Data")
        # fetch_employee_data()
    elif user_input == "3":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")

def fetch_student_data():
    print("Fetching student data...")
    # student_data = fetch_student_data_from_db()
    # print(student_data)

def fetch_employee_data():
    print("Fetching employee data...")
    # employee_data = fetch_employee_data_from_db()
    # print(employee_data)

