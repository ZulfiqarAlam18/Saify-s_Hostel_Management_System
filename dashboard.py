import main
from db_helper import connect_db

def dashboard():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Example: Fetch and display data insights
        cursor.execute('''
        SELECT COUNT(*) FROM students
        ''')
        student_count = cursor.fetchone()[0]

        cursor.execute('''
        SELECT COUNT(*) FROM employees
        ''')
        employee_count = cursor.fetchone()[0]

        cursor.execute('''
        SELECT AVG(amount) FROM salaries
        ''')
        average_salary = cursor.fetchone()[0]

        print("Dashboard Insights:")
        print(f"Total Students: {student_count}")
        print(f"Total Employees: {employee_count}")
        print(f"Average Salary: {average_salary}")

        conn.close()
    except Exception as e:
        print("An error occurred while fetching dashboard data:", str(e))

    print("Under Construction..............")
    main.main()