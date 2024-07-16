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
        cnic_no = input("CNIC Number: ")
        room_no = input("Room Number: ")
        uni_name = input("University Name: ")
        address = input("Address: ")
        district = input("District: ")
        
        query = """
        INSERT INTO students (name, f_name, phone_no, cnic_no, room_no, uni_name, address, district)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (name, f_name, phone_no, cnic_no, room_no, uni_name, address, district)
        db_helper.execute_query(query, params)
        
        print("Student added successfully.")
        students()
    except Exception as e:
        print(f"Error: {e}")

def update_student_data():
    try:
        student_id = input("Enter Student ID: ")
        data_choice = input("Update What? (1.Name, 2.Phone Number, 3.Father's Name, 4.CNIC Number, 5.Address, 6.District, 7.Room Number, 8.University Name): ")
        
        column_map = {
            "1": "name",
            "2": "phone_no",
            "3": "f_name",
            "4": "cnic_no",
            "5": "address",
            "6": "district",
            "7": "room_no",
            "8": "uni_name"
        }
        
        if data_choice in column_map:
            new_value = input(f"Enter new value for {column_map[data_choice]}: ")
            query = f"UPDATE students SET {column_map[data_choice]} = ? WHERE id = ?"
            params = (new_value, student_id)
            db_helper.execute_query(query, params)
            print("Student data updated successfully.")
            students()
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")

def remove_student():
    try:
        student_id = input("Enter Student ID to remove: ")
        query = "DELETE FROM students WHERE id = ?"
        params = (student_id,)
        db_helper.execute_query(query, params)
        print("Student removed successfully.")
        students()
    except Exception as e:
        print(f"Error: {e}")

def view_students():
    try:
        query = "SELECT * FROM students"
        students_list = db_helper.fetch_query(query)
        for student in students_list:
            print(student)
        
        print("--------------------------------")
        students()
    except Exception as e:
        print(f"Error: {e}")
