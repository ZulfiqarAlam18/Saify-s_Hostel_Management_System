import main
import db_helper

def dashboard():
    try:
        print("Generating Insights...")
        
        # Total students
        query = "SELECT COUNT(*) FROM students"
        total_students = db_helper.fetch_query(query)[0][0]
        
        # Total employees
        query = "SELECT COUNT(*) FROM employees"
        total_employees = db_helper.fetch_query(query)[0][0]
        
        # Total tasks
        query = "SELECT COUNT(*) FROM tasks"
        total_tasks = db_helper.fetch_query(query)[0][0]
        
        # Total finance (incomes and expenses)
        query = "SELECT category, SUM(amount) FROM finance GROUP BY category"
        finance_summary = db_helper.fetch_query(query)
        
        print(f"Total Students: {total_students}")
        print(f"Total Employees: {total_employees}")
        print(f"Total Tasks: {total_tasks}")
        print("Finance Summary:")
        for category, amount in finance_summary:
            print(f"{category}: {amount}")
        
        main.main()
    except Exception as e:
        print(f"Error: {e}")
