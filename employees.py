import main
import db_helper

def employees():
    user_input = input("""--------------------------------
    1. Add employee
    2. Remove employee
    3. Update employee's data
    4. View List of employees
    5. Back to Main Menu
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
    try:
        name = input("Name: ")
        f_name = input("Father Name: ")
        phone_no = input("Phone Number: ")
        cnic_no = input("Cnic Number: ")
        address = input("Address: ")
        district = input("District: ")

        query = "INSERT INTO employees (name, father_name, phone_no, cnic_no, address, district) VALUES (?, ?, ?, ?, ?, ?)"
        db_helper.execute_query(query, (name, f_name, phone_no, cnic_no, address, district))
        
        print("Added Successfully")
        employees()
    except Exception as e:
        print(f"Error: {e}")

def update_employee_data():
    try:
        name = input("Enter Employee Name: ")
        data = input("Update What (1.Name, 2.Phone Number, 3.Father Name, 4.Cnic Number, 5.Address, 6.District): ")
        new_value = input("Enter new value: ")

        fields = {
            "1": "name",
            "2": "phone_no",
            "3": "father_name",
            "4": "cnic_no",
            "5": "address",
            "6": "district"
        }

        if data in fields:
            query = f"UPDATE employees SET {fields[data]} = ? WHERE name = ?"
            db_helper.execute_query(query, (new_value, name))
            print("Updated Successfully")
            employees()
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")

def remove_employee():
    try:
        name = input("Enter Employee Name: ")
        query = "DELETE FROM employees WHERE name = ?"
        db_helper.execute_query(query, (name,))
        print("Removed Successfully")
        employees()
    except Exception as e:
        print(f"Error: {e}")

def view_employees():
    try:
        query = "SELECT * FROM employees"
        employees = db_helper.fetch_query(query)
        for employee in employees:
            print(employee)
            print("--------------------------------")
            employees()
    except Exception as e:
        print(f"Error: {e}")
