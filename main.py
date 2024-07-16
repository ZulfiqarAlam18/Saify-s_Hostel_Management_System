import finance
import students
import employees
import to_do_list
import dashboard
import history

def main():
    user_input = input("""--------------------------------
    1. Finance
    2. Students
    3. Employees
    4. To-Do List
    5. Dashboard
    6. History
    7. Exit
    Enter choice (Number):""")
    
    if user_input == "1":
        finance.finance()
    elif user_input == "2":
        students.students()
    elif user_input == "3":
        employees.employees()
    elif user_input == "4":
        to_do_list.to_do_list()
    elif user_input == "5":
        dashboard.dashboard()
    elif user_input == "6":
        history.history()
    elif user_input == "7":
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
