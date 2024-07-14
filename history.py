
def history():
    user_input = input("Enter choice (Number):\n1.Student Data\n2.Employee Data\n3. Back to Menu\n:")
    
    if user_input == "1":
        print("Student Data")
        # fetch_student_data()
    elif user_input == "2":
        print("Employee Data")
        # fetch_employee_data()
    elif user_input == "3":
        print("Getting back to menu...")
        # main()
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

