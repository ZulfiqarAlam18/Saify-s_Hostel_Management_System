import main
from db_helper import connect_db

def employees():
    user_input = input("""--------------------------------
    1. Add employee
    2. Remove employee
    3. Update employee's data
    4. View List of employees
    5. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        add_employee()
    elif user_input == "2":
        remove_employee()
    elif user_input == "3":
        update_employee_data()
    elif user_input == "4":
        view_employees()
    elif user_input == "5":
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_employee():
    name = input("Name:")
    f_name = input("Father's Name:")
    phone_no = input("Phone Number:")
    cnic_no = input("CNIC Number:")
    address = input("Address:")
    district = input("District:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO employees (name, father_name, phone_no, cnic_no, address, district)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, f_name, phone_no, cnic_no, address, district))
        conn.commit()
        conn.close()
        print("Employee added successfully.")
    except Exception as e:
        print("An error occurred while adding employee:", str(e))

def update_employee_data():
    employee_id = input("Enter Employee ID:")
    column = input("Update Which Field (name, father_name, phone_no, cnic_no, address, district):")
    new_value = input(f"Enter New Value for {column}:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f'''
        UPDATE employees
        SET {column} = ?
        WHERE id = ?
        ''', (new_value, employee_id))
        conn.commit()
        conn.close()
        print("Employee data updated successfully.")
    except Exception as e:
        print("An error occurred while updating employee data:", str(e))

def remove_employee():
    employee_id = input("Enter Employee ID to remove:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM employees WHERE id = ?
        ''', (employee_id,))
        conn.commit()
        conn.close()
        print("Employee removed successfully.")
    except Exception as e:
        print("An error occurred while removing employee:", str(e))

def view_employees():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM employees
        ''')
        employees = cursor.fetchall()
        conn.close()

        print("List of Employees:")
        for employee in employees:
            print(employee)
    except Exception as e:
        print("An error occurred while fetching employees:", str(e))
