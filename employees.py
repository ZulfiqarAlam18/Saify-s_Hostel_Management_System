
def employees():
    user_input = input("""Enter choice (Number)
                       1. Add employee
                       2. Remove employee
                       3. Update employee's data
                       4. View List of employees
                       5. Back to Menu\n""")
    
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
        #break
    else:
        print("Invalid choice. Please try again.")

employees()

