import finance
import students
import employees
import dashboard
import history
import to_do_list

def main_menu():
    return input("""--------------------------------
                   "Saif's Hostel Management System"
    1. Finance
    2. Student Affairs
    3. Employees
    4. To Do List
    5. History
    6. Dashboard
    7. Exit
    Enter choice (Number): """)

def main():
    while True:
        try:
            user_input = main_menu()
        
            if user_input == "1":
                finance.finance()
            elif user_input == "2":
                students.students()
            elif user_input == "3":
                employees.employees()
            elif user_input == "4":
                to_do_list.to_do_list()
            elif user_input == "5":
                history.history()
            elif user_input == "6":
                dashboard.dashboard()
            elif user_input == "7":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 to 8.")
        except Exception as e:
            print("An error occurred:", str(e))
            continue

if __name__ == "__main__":
    main()
