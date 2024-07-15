import fee_section
import students
import employees
import dashboard
import history
import finance
import to_do_list

def main_menu():
    print("--------------------------------")
    print("       Saif's Hostel Management System       ")
    print("1. Fee Section")
    print("2. Student Affairs")
    print("3. Employees")
    print("4. To Do List")
    print("5. Finance")
    print("6. History")
    print("7. Dashboard")
    print("8. Exit")
    return input("Enter choice (Number): ")

def main():
    while True:
        user_input = main_menu()
        
        if user_input == "1":
            fee_section.fee_section()
        elif user_input == "2":
            students.students()
        elif user_input == "3":
            employees.employees()
        elif user_input == "4":
            to_do_list.to_do_list()
        elif user_input == "5":
            finance.finance()
        elif user_input == "6":
            history.history()
        elif user_input == "7":
            dashboard.dashboard()
        elif user_input == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
