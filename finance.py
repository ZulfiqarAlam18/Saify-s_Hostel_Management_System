
def finance():
    user_input = input("Enter choice (Number):\n1. View this Month's Expenditures\n2. View this month's Fee's received\n3. Enter Expendtures\n4. Back to Menu")

    if user_input == "1":
        print("Viewing this Month's Expenditures")
        # view_this_month_expenditures()
    elif user_input == "2":
        print("Viewing this Month's Fee's Received")
        # view_this_month_fees_received()
    elif user_input == "3":
        print("Entering Expenditures")
        # enter_expenditures()
    elif user_input == "4":
        print("Getting back to menu...")
        # main()
    else:
        print("Invalid choice. Please try again.")

def view_this_month_expenditures():
    print("This Month's Expenditures")
    # fetch_this_month_expenditures()

def view_this_month_fees_received():
    print("This Month's Fee's Received")
    # fetch_this_month_fees_received()

def enter_expenditures():
    print("Entering Expenditures")
    # add_expenditure()
    # update_expenditure_table()

