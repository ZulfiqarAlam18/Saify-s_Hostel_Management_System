import main

def students():
    user_input = input("""--------------------------------
    1. Add student
    2. Remove student
    3. Update student's data
    4. View List of students
    5. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        print("Adding student")
        add_student()
    elif user_input == "2":
        print("Removing student")
        remove_student()
    elif user_input == "3":
        print("Updating student's data")
        update_student_data()
    elif user_input == "4":
        print("Viewing List of students")
        view_students()
    elif user_input == "5":
        print("Getting back to menu...")
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_student():
    name = input("Name:")
    f_name = input("Father's Name:")
    phone_no = input("Phone Number:")
    cnic_no = input("Cnic Number:")
    room_no = input("Room Number:")
    Uni_name = input("University Name:")
    address = input("Address:")
    district = input("District:")
    print("Added Successfully")

def update_student_data():
    name = input("Enter student Name:")
    data = input("Update What 1.Name:\n2.Phone Number\n3.Father Name:\n4.Cnic Number\n5.Address\n6.District\n7. Room Number:\n8.UNi_Name")
    print("Updated Successfully")
def remove_student():
    name = input("Enter student Name:")
    print("Removed Successfully")
def view_students():
    print("List of students")
    # fetch_students()


