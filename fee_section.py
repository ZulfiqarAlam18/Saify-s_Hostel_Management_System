
import main
def fee_section():
    user_input = input("""--------------------------------
    1. Fee Entry
    2. Unpiad students
    3. Paid students
    4. Unpaid employees
    5. paid employees
    6. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        print("Fee Entry")
        # fee_entry()
    elif user_input == "2":
        print("Unpaid students")
        # unpaid_students()
    elif user_input == "3":
        print("Paid students")
        # paid_students()
    elif user_input == "4":
        print("Unpaid employees")
        # unpaid_employees()
    elif user_input == "5":
        print("Paid employees")
        # paid_employees()
    elif user_input == "6":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")
    

def fee_entry():
    print("Fee Entry")
    # add_fee_entry()

def unpaid_students():
    print("Unpaid students")
    # fetch_unpaid_students()

def paid_students():
    print("Paid students")
    # fetch_paid_students()

def unpaid_employees():
    print("Unpaid employees")
    # fetch_unpaid_employees()

def paid_employees():
    print("Paid employees")
    # fetch_paid_employees()

    