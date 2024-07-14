

    
while True:
    def fee_section():
        print("Under Construction")
    def student_affairs():
        print("Under Construction")
    def employees():
        print("Under Construction")
    def to_do_list():
        print("Under Construction")
    def expenditure():
        print("Under Construction")
    def history():
        print("Under Construction")
    def finance():
        print("Under Construction")
    
    while True:
        user_input = input("""Enter choice(Number):
                1. Fee Section
                2. Student Affairs
                3. Employees
                4. To Do list
                5. Expenditure
                6. History
                7. Finance
                8. Exit\n\t:""")
    
        if user_input == "1":
            fee_section()
        elif user_input == "2":
            student_affairs()
        elif user_input == "3":
            employees()
        elif user_input == "4":
            to_do_list()
        elif user_input == "5":
            expenditure()
        elif user_input == "6":
            history()
        elif user_input == "7":
            finance()
        elif user_input == "8":
            break
        else:
            print("Invalid choice. Please try again.")
            