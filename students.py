import main
import db_helper

def students():
    user_input = input("""--------------------------------
    1. Add student
    2. Remove student
    3. Update student's data
    4. View List of students
    5. Back to Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        add_student()
    elif user_input == "2":
        remove_student()
    elif user_input == "3":
        update_student_data()
    elif user_input == "4":
        view_students()
    elif user_input == "5":
        main.main()
    else:
        print("Invalid choice. Please try again.")

def add_student():
    try:
        name = input("Name: ")
        f_name = input("Father's Name: ")
        phone_no = input("Phone Number: ")
        cnic_no = input("Cnic Number: ")
        room_no = input("Room Number: ")
        uni_name = input("University Name: ")
        address = input("Address: ")
        district = input("District: ")

        query = "INSERT INTO students (name, father_name, phone_no, cnic_no, room_no, university_name, address, district) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        db_helper.execute_query(query, (name, f_name, phone_no, cnic_no, room_no, uni_name, address, district))
        
        print("Added Successfully")
    except Exception as e:
        print(f"Error: {e}")

def update_student_data():
    try:
        name = input("Enter student Name: ")
        data = input("Update What (1.Name, 2.Phone Number, 3.Father Name, 4.Cnic Number, 5.Address, 6.District, 7.Room Number, 8.University Name): ")
        new_value = input("Enter new value: ")

        fields = {
            "1": "name",
            "2": "phone_no",
            "3": "father_name",
            "4": "cnic_no",
            "5": "address",
            "6": "district",
            "7": "room_no",
            "8": "university_name"
        }

        if data in fields:
            query = f"UPDATE students SET {fields[data]} = ? WHERE name = ?"
            db_helper.execute_query(query, (new_value, name))
            print("Updated Successfully")
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")

def remove_student():
    try:
        name = input("Enter student Name: ")
        query = "DELETE FROM students WHERE name = ?"
        db_helper.execute_query(query, (name,))
        print("Removed Successfully")
    except Exception as e:
        print(f"Error: {e}")

def view_students():
    try:
        query = "SELECT * FROM students"
        students = db_helper.fetch_query(query)
        for student in students:
            print(student)
    except Exception as e:
        print(f"Error: {e}")
