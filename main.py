import fee_section
import students
import employees
import dashboard
import history
import finance
import to_do_list


    
while True:
    user_input = input("""Enter choice(Number):
                1. Fee Section
                2. Student Affairs
                3. Employees
                4. To Do list
                5. Finance
                6. History
                7. Dashboard
                8. Exit\n\t:""")
    
    if user_input == "1":
            fee_section()
    elif user_input == "2":
            students()
    elif user_input == "3":
            employees()
    elif user_input == "4":
            to_do_list()
    elif user_input == "5":
            finance()
    elif user_input == "6":
            history()
    elif user_input == "7":
            dashboard()
    elif user_input == "8":
            break
    else:
            print("Invalid choice. Please try again.")
            