import main
from db_helper import connect_db

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
    name = input("Name:")
    f_name = input("Father's Name:")
    phone_no = input("Phone Number:")
    cnic_no = input("CNIC Number:")
    room_no = input("Room Number:")
    uni_name = input("University Name:")
    address = input("Address:")
    district = input("District:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO students (name, father_name, phone_no, cnic_no, room_no, uni_name, address, district)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, f_name, phone_no, cnic_no, room_no, uni_name, address, district))
        conn.commit()
        conn.close()
        print("Student added successfully.")
    except Exception as e:
        print("An error occurred while adding student:", str(e))

def update_student_data():
    student_id = input("Enter Student ID:")
    column = input("Update Which Field (name, father_name, phone_no, cnic_no, room_no, uni_name, address, district):")
    new_value = input(f"Enter New Value for {column}:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f'''
        UPDATE students
        SET {column} = ?
        WHERE id = ?
        ''', (new_value, student_id))
        conn.commit()
        conn.close()
        print("Student data updated successfully.")
    except Exception as e:
        print("An error occurred while updating student data:", str(e))

def remove_student():
    student_id = input("Enter Student ID to remove:")

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM students WHERE id = ?
        ''', (student_id,))
        conn.commit()
        conn.close()
        print("Student removed successfully.")
    except Exception as e:
        print("An error occurred while removing student:", str(e))

def view_students():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM students
        ''')
        students = cursor.fetchall()
        conn.close()

        print("List of Students:")
        for student in students:
            print(student)
    except Exception as e:
        print("An error occurred while fetching students:", str(e))
