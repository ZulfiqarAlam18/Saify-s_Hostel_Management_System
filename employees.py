import main
def employees():
    user_input = input("""--------------------------------
    1. Add employee
    2. Remove employee
    3. Update employee's data
    4. View List of employees
    5. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        print("Adding employee")
        # add_employee()
    elif user_input == "2":
        print("Removing employee")
        # remove_employee()
    elif user_input == "3":
        print("Updating employee's data")
        # update_employee_data()
    elif user_input == "4":
        print("Viewing List of employees")
        # view_employees()
    elif user_input == "5":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_employee():
    name = input("Name:")
    f_name = input("Father Name:")
    phone_no = input("Phone Number:")
    cnic_no = input("Cnic Number:")
    address = input("Address:")
    district = input("District:")
    print("Added Successfully")

def update_employee_data():
    name = input("Enter Employee Name:")
    data = input("Update What 1.Name:\n2.Phone Number\n3.Father Name:\n4.Cnic Number\n5.Address\n6.District")
    print("Updated Successfully")
def remove_employee():
    name = input("Enter Employee Name:")
    print("Removed Successfully")
def view_employees():
    print("List of Employees")
    # fetch_employees()
def back_to_menu():
    print("Getting back to menu...")
    main()




