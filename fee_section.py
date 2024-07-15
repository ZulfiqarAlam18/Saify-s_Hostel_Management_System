
import main
def fee_section():
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
        print("Adding Fee")
        # add_fee()
    elif user_input == "2":
        print("Adding Employee Salary")
        # add_employee_salary()
    elif user_input == "3":
        print("Adding Expenditures")
        # add_expenditure()
    elif user_input == "4":
        print("Paid students")
        # paid_students()
    elif user_input == "5":
        print("Unpaid students")
        # unpaid_students()
    elif user_input == "6":
        print("Paid employees")
        # paid_employees()
    elif user_input == "7":
        print("Unpaid employees")
        # unpaid_employees()
    elif user_input == "8":
        print("Monthly Report")
        # monthly_report()
    elif user_input == "9":
        print("Yearly Report")
        # yearly_report()
    elif user_input == "10":
        print("Getting back to main menu")

def add_fee():
    print("Enter fee details here")
    # add_fee_details()

def add_employee_salary():
    print("Enter employee salary details here")
    # add_employee_salary_details()


def paid_students():
    print("Enter paid student details here")
    # paid_student_details()

def unpaid_students():
    print("Enter unpaid student details here")
    # unpaid_student_details()

def paid_employees():
    print("Enter paid employee details here")
    # paid_employee_details()

def unpaid_employees():
    print("Enter unpaid employee details here")
    # unpaid_employee_details()

def monthly_report():
    print("Generating monthly report here")
    # generate_monthly_report()

def yearly_report():
    print("Generating yearly report here")
    # generate_yearly_report()

def add_expenditure():
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

def add_all_expenditures():
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


def add_single_expenditure():
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
