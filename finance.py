import main
from db_helper import connect_db

def finance():
    user_input = input("""--------------------------------
    1. Pay Fees
    2. Pay Salary
    3. Expenditures
    4. Paid Employees
    5. Unpaid Employees
    6. Monthly Report
    7. Yearly Report
    8. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        pay_fees()
    elif user_input == "2":
        pay_salary()
    elif user_input == "3":
        expenditures()
    elif user_input == "4":
        paid_employees()
    elif user_input == "5":
        unpaid_employees()
    elif user_input == "6":
        monthly_report()
    elif user_input == "7":
        yearly_report()
    elif user_input == "8":
        main.main()
    else:
        print("Invalid choice. Please try again.")

def pay_fees():
    student_id = input("Enter Student ID:")
    amount = input("Enter Amount:")
    date = input("Enter Date (YYYY-MM-DD):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO fees (student_id, amount, date, paid)
        VALUES (?, ?, ?, 1)
        ''', (student_id, amount, date))
        conn.commit()
        conn.close()
        print("Fees paid successfully.")
    except Exception as e:
        print("An error occurred while paying fees:", str(e))

def pay_salary():
    employee_id = input("Enter Employee ID:")
    amount = input("Enter Amount:")
    date = input("Enter Date (YYYY-MM-DD):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO salaries (employee_id, amount, date, paid)
        VALUES (?, ?, ?, 1)
        ''', (employee_id, amount, date))
        conn.commit()
        conn.close()
        print("Salary paid successfully.")
    except Exception as e:
        print("An error occurred while paying salary:", str(e))

def expenditures():
    category = input("Enter Expenditure Category:")
    amount = input("Enter Amount:")
    date = input("Enter Date (YYYY-MM-DD):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO expenditures (category, amount, date)
        VALUES (?, ?, ?)
        ''', (category, amount, date))
        conn.commit()
        conn.close()
        print("Expenditure added successfully.")
    except Exception as e:
        print("An error occurred while adding expenditure:", str(e))

def paid_employees():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM salaries WHERE paid = 1
        ''')
        paid_employees = cursor.fetchall()
        conn.close()

        print("Paid Employees:")
        for employee in paid_employees:
            print(employee)
    except Exception as e:
        print("An error occurred while fetching paid employees:", str(e))

def unpaid_employees():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM salaries WHERE paid = 0
        ''')
        unpaid_employees = cursor.fetchall()
        conn.close()

        print("Unpaid Employees:")
        for employee in unpaid_employees:
            print(employee)
    except Exception as e:
        print("An error occurred while fetching unpaid employees:", str(e))

def monthly_report():
    month = input("Enter Month (MM):")
    year = input("Enter Year (YYYY):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM expenditures WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        ''', (month, year))
        expenditures = cursor.fetchall()
        cursor.execute('''
        SELECT * FROM fees WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        ''', (month, year))
        fees = cursor.fetchall()
        cursor.execute('''
        SELECT * FROM salaries WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        ''', (month, year))
        salaries = cursor.fetchall()
        conn.close()

        print("Monthly Report:")
        print("Expenditures:", expenditures)
        print("Fees:", fees)
        print("Salaries:", salaries)
    except Exception as e:
        print("An error occurred while generating the monthly report:", str(e))

def yearly_report():
    year = input("Enter Year (YYYY):")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM expenditures WHERE strftime('%Y', date) = ?
        ''', (year,))
        expenditures = cursor.fetchall()
        cursor.execute('''
        SELECT * FROM fees WHERE strftime('%Y', date) = ?
        ''', (year,))
        fees = cursor.fetchall()
        cursor.execute('''
        SELECT * FROM salaries WHERE strftime('%Y', date) = ?
        ''', (year,))
        salaries = cursor.fetchall()
        conn.close()

        print("Yearly Report:")
        print("Expenditures:", expenditures)
        print("Fees:", fees)
        print("Salaries:", salaries)
    except Exception as e:
        print("An error occurred while generating the yearly report:", str(e))














  # generate_yearly_report()

#def add_expenditure():
    user_input = input("""
    1. All
    2. Single Item
    3. Back to Main Menu
    Enter choice (Number):""")

    if user_input == "1":
        print("Adding expenditure for all items")
        add_all_expenditures()
    elif user_input == "2":
        print("Adding expenditure for a single item")
        add_single_expenditure()
    elif user_input == "3":
        print("Getting back to main menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")

#def add_all_expenditures():
    print("Enter Amounts one by one:")
    meal = int(input("Meal(breaf fast,Lunch,Dinner etc):"))
    gas_bill = int(input("Gas Bill:"))
    electricity = int(input("Electricity:"))
    rent = int(input("Rental charges:"))
    wifi_bills = int(input("Wifi Bills:"))
    tax = int(input("Taxes:"))
    water = int(input("Water charges:"))
    employees = int(input("Employees"))
    expenditures = int(input("Expenditure:"))
    others = int(input("Other :"))
    total_expenditure = meal + gas_bill + electricity + rent + tax + employees +  water + expenditures + wifi_bills + others
    print("Total Expenditure:", total_expenditure)


#def add_single_expenditure():
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
    10. Wifi bills
    11. Others
    12. One step Back
    13. Back to main menu
    Choose Item Number""")
    if user_input == "1":
        meal = int(input("Meal Expenditure:"))
        #update_expenditure_table(meal)
    elif user_input == "2":
        gas_bill = int(input("Gas Bill Expenditure:"))
       # update_expenditure_table(gas_bill)
    elif user_input == "3":
        electricity = int(input("Electricity Bill Expenditure:"))
        #update_expenditure_table(electricity)
    elif user_input == "4":
        rent = int(input("Rental Charges Expenditure:"))
        #update_expenditure_table(rent)
    elif user_input == "5":
        wifi_bills = int(input("Wifi Bills Expenditure:"))
       # update_expenditure_table(wifi_bills)
    elif user_input == "6":
        tax = int(input("Taxes Expenditure:"))
       # update_expenditure_table(tax)
    elif user_input == "7":
        water = int(input("Water Charges Expenditure:"))
        #update_expenditure_table(water)
    elif user_input == "8":
        employees = int(input("Employee Salaries Expenditure:"))
        #update_expenditure_table(employees)
    elif user_input == "9":
        expenditure = int(input("Expenditure Expenditure:"))
        #update_expenditure_table(expenditure)
    elif user_input == "10":
        wifi_bills = int(input("Wifi Bills Expenditure:"))
        #update_expenditure_table(wifi_bills)
    elif user_input == "11":
        others = int(input("Others Expenditure:"))
        #update_expenditure_table(others)
    elif user_input == "12":
        print("One step back...")
        add_single_expenditure()
    elif user_input == "13":
        print("Getting back to main menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")
    



# TODO: Implement database operations for fee_section functions
