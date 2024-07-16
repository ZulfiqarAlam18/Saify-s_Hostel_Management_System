import main
import db_helper

def finance():
    user_input = input("""--------------------------------
    1. Add Fee
    2. Add Employee Salary
    3. Add Expenditures
    4. Paid students
    5. Unpaid students
    6. Paid employees
    7. Unpaid employees
    8. Monthly Report
    9. Yearly Report                  
    10. Back to Main Menu
    Enter choice (Number):""")

    if user_input == "1":
        add_fee()
    elif user_input == "2":
        add_employee_salary()
    elif user_input == "3":
        add_expenditure()
    elif user_input == "4":
        paid_students()
    elif user_input == "5":
        unpaid_students()
    elif user_input == "6":
        paid_employees()
    elif user_input == "7":
        unpaid_employees()
    elif user_input == "8":
        monthly_report()
    elif user_input == "9":
        yearly_report()
    elif user_input == "10":
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_fee():
    try:
        student_id = input("Enter Student ID: ")
        amount = input("Enter Fee Amount: ")

        query = "UPDATE students SET paid = 1 WHERE id = ?"
        db_helper.execute_query(query, (student_id,))

        query = "INSERT INTO finance (category, amount, date) VALUES (?, ?, DATE('now'))"
        db_helper.execute_query(query, ("Fee", amount))
        
        print("Fee added successfully.")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def add_employee_salary():
    try:
        employee_id = input("Enter Employee ID: ")
        amount = input("Enter Salary Amount: ")

        query = "UPDATE employees SET paid = 1 WHERE id = ?"
        db_helper.execute_query(query, (employee_id,))

        query = "INSERT INTO finance (category, amount, date) VALUES (?, ?, DATE('now'))"
        db_helper.execute_query(query, ("Salary", amount))
        
        print("Salary added successfully.")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def add_expenditure():
    user_input = input("""
    1. All
    2. Single Item
    3. Back to Main Menu
    Enter choice (Number):""")

    if user_input == "1":
        add_all_expenditures()
    elif user_input == "2":
        add_single_expenditure()
    elif user_input == "3":
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_all_expenditures():
    try:
        meal = int(input("Meal (breakfast, lunch, dinner, etc): "))
        gas_bill = int(input("Gas Bill: "))
        electricity = int(input("Electricity: "))
        rent = int(input("Rental charges: "))
        wifi_bills = int(input("Wifi Bills: "))
        tax = int(input("Taxes: "))
        water = int(input("Water charges: "))
        employees = int(input("Employees: "))
        expenditures = int(input("Expenditure: "))
        others = int(input("Other: "))

        total_expenditure = meal + gas_bill + electricity + rent + wifi_bills + tax + water + employees + expenditures + others

        query = "INSERT INTO finance (category, amount, date) VALUES (?, ?, DATE('now'))"
        db_helper.execute_query(query, ("Expenditure", total_expenditure))

        print("Total Expenditure:", total_expenditure)
        finance()
    except Exception as e:
        print(f"Error: {e}")

def add_single_expenditure():
    try:
        user_input = input("""
        1. Meal Expenditures 
        2. Gas Bill
        3. Electricity bills
        4. Rental Charges
        5. Wifi Bills
        6. Taxes
        7. Water Charges
        8. Employee Salaries
        9. Expenditure
        10. Others
        11. One step Back
        12. Back to main menu
        Choose Item Number: """)
        
        category_map = {
            "1": "Meal",
            "2": "Gas Bill",
            "3": "Electricity",
            "4": "Rent",
            "5": "Wifi Bills",
            "6": "Taxes",
            "7": "Water Charges",
            "8": "Employee Salaries",
            "9": "Expenditure",
            "10": "Others"
        }
        
        if user_input in category_map:
            amount = int(input(f"Enter amount for {category_map[user_input]}: "))
            query = "INSERT INTO finance (category, amount, date) VALUES (?, ?, DATE('now'))"
            db_helper.execute_query(query, (category_map[user_input], amount))
            print(f"{category_map[user_input]} expenditure added successfully.")

            finance()
        elif user_input == "11":
            add_single_expenditure()
        elif user_input == "12":
            main.main()
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")

def paid_students():
    try:
        query = "SELECT * FROM students WHERE paid = 1"
        students = db_helper.fetch_query(query)
        for student in students:
            print(student)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def unpaid_students():
    try:
        query = "SELECT * FROM students WHERE paid = 0"
        students = db_helper.fetch_query(query)
        for student in students:
            print(student)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def paid_employees():
    try:
        query = "SELECT * FROM employees WHERE paid = 1"
        employees = db_helper.fetch_query(query)
        for employee in employees:
            print(employee)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def unpaid_employees():
    try:
        query = "SELECT * FROM employees WHERE paid = 0"
        employees = db_helper.fetch_query(query)
        for employee in employees:
            print(employee)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def monthly_report():
    try:
        query = "SELECT * FROM finance WHERE date >= DATE('now', 'start of month')"
        report = db_helper.fetch_query(query)
        for record in report:
            print(record)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")

def yearly_report():
    try:
        query = "SELECT * FROM finance WHERE date >= DATE('now', 'start of year')"
        report = db_helper.fetch_query(query)
        for record in report:
            print(record)
        
        print("--------------------------------")
        finance()
    except Exception as e:
        print(f"Error: {e}")











