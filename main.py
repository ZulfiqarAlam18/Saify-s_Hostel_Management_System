import fee_section
import students
import employees
import dashboard
import history
import finance
import to_do_list

def main_menu():
    return input("""--------------------------------
                   "Saif's Hostel Management System"
    1. Fee Section
    2. Student Affairs
    3. Employees
    4. To Do List
    5. Finance
    6. History
    7. Dashboard
    8. Exit
    Enter choice (Number): """)

def main():
    while True:
        try:
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
                print("Invalid choice. Please enter a number between 1 to 8.")
        except Exception as e:
            print("An error occurred:", str(e))
            continue

if __name__ == "__main__":
    main()
