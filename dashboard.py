import main
import db_helper
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def fetch_query_result(query):
    try:
        return db_helper.fetch_query(query)
    except Exception as e:
        print(f"Error fetching query result: {e}")
        return []

def plot_bar_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 5))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()

def plot_pie_chart(data, title, filename):
    plt.figure(figsize=(10, 5))
    data.plot(kind='pie', autopct='%1.1f%%')
    plt.title(title)
    plt.ylabel('')
    plt.savefig(filename)
    plt.close()

def plot_line_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 5))
    data.plot(kind='line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()

def dashboard():
    try:
        print("Generating Insights...")

        # Total students
        query = "SELECT COUNT(*) FROM students"
        total_students = fetch_query_result(query)[0][0]

        # New admissions and departures per month
        query = """
        SELECT strftime('%Y-%m', admission_date) as month, COUNT(*) as count
        FROM students
        GROUP BY month
        """
        admissions = fetch_query_result(query)
        admissions_df = pd.DataFrame(admissions, columns=['Month', 'Admissions'])

        query = """
        SELECT strftime('%Y-%m', departure_date) as month, COUNT(*) as count
        FROM students
        GROUP BY month
        """
        departures = fetch_query_result(query)
        departures_df = pd.DataFrame(departures, columns=['Month', 'Departures'])

        # Room occupancy rates
        query = "SELECT room_number, COUNT(*) FROM students GROUP BY room_number"
        room_occupancy = fetch_query_result(query)
        room_occupancy_df = pd.DataFrame(room_occupancy, columns=['Room', 'Occupancy'])

        # Average length of stay
        query = "SELECT AVG(JULIANDAY(departure_date) - JULIANDAY(admission_date)) FROM students"
        avg_length_of_stay = fetch_query_result(query)[0][0]

        # Total employees
        query = "SELECT COUNT(*) FROM employees"
        total_employees = fetch_query_result(query)[0][0]

        # Salaries paid and pending
        query = "SELECT status, SUM(amount) FROM salaries GROUP BY status"
        salaries_summary = fetch_query_result(query)
        salaries_summary_df = pd.DataFrame(salaries_summary, columns=['Status', 'Amount'])

        # Employee attendance
        query = "SELECT employee_id, COUNT(*) FROM attendance WHERE status='Present' GROUP BY employee_id"
        employee_attendance = fetch_query_result(query)
        employee_attendance_df = pd.DataFrame(employee_attendance, columns=['Employee ID', 'Days Present'])

        # Employee performance
        query = "SELECT employee_id, AVG(performance_rating) FROM performance_reviews GROUP BY employee_id"
        employee_performance = fetch_query_result(query)
        employee_performance_df = pd.DataFrame(employee_performance, columns=['Employee ID', 'Average Rating'])

        # Total tasks
        query = "SELECT COUNT(*) FROM tasks"
        total_tasks = fetch_query_result(query)[0][0]

        # Completed and pending tasks
        query = "SELECT status, COUNT(*) FROM tasks GROUP BY status"
        tasks_summary = fetch_query_result(query)
        tasks_summary_df = pd.DataFrame(tasks_summary, columns=['Status', 'Count'])

        # Task deadlines
        query = "SELECT description, due_date FROM tasks WHERE due_date >= date('now') ORDER BY due_date ASC"
        upcoming_deadlines = fetch_query_result(query)
        upcoming_deadlines_df = pd.DataFrame(upcoming_deadlines, columns=['Description', 'Due Date'])

        # Maintenance logs
        query = "SELECT description, date FROM maintenance WHERE status='Completed'"
        completed_maintenance = fetch_query_result(query)

        query = "SELECT description, date FROM maintenance WHERE status='Pending'"
        pending_maintenance = fetch_query_result(query)

        # Finance summary
        query = "SELECT category, SUM(amount) FROM finance GROUP BY category"
        finance_summary = fetch_query_result(query)
        finance_summary_df = pd.DataFrame(finance_summary, columns=['Category', 'Amount'])

        # Automated suggestions and alerts
        overdue_tasks_query = "SELECT description FROM tasks WHERE due_date < date('now') AND status='Pending'"
        overdue_tasks = fetch_query_result(overdue_tasks_query)
        
        overdue_payments_query = "SELECT description FROM finance WHERE due_date < date('now') AND status='Pending'"
        overdue_payments = fetch_query_result(overdue_payments_query)

        pending_maintenance_query = "SELECT description FROM maintenance WHERE status='Pending'"
        pending_maintenance_requests = fetch_query_result(pending_maintenance_query)

        # User feedback
        query = "SELECT feedback FROM user_feedback"
        user_feedback = fetch_query_result(query)

        # Generating Reports
        admissions_df.to_csv('admissions_report.csv')
        departures_df.to_csv('departures_report.csv')
        room_occupancy_df.to_csv('room_occupancy_report.csv')
        salaries_summary_df.to_csv('salaries_report.csv')
        employee_attendance_df.to_csv('employee_attendance_report.csv')
        employee_performance_df.to_csv('employee_performance_report.csv')
        tasks_summary_df.to_csv('tasks_report.csv')
        upcoming_deadlines_df.to_csv('upcoming_deadlines_report.csv')
        finance_summary_df.to_csv('finance_report.csv')

        # Plotting Visual Representations
        plot_bar_chart(admissions_df.set_index('Month'), 'Monthly Admissions', 'Month', 'Admissions', 'admissions_chart.png')
        plot_bar_chart(departures_df.set_index('Month'), 'Monthly Departures', 'Month', 'Departures', 'departures_chart.png')
        plot_bar_chart(room_occupancy_df.set_index('Room'), 'Room Occupancy Rates', 'Room', 'Occupancy', 'room_occupancy_chart.png')
        plot_bar_chart(salaries_summary_df.set_index('Status'), 'Salaries Summary', 'Status', 'Amount', 'salaries_chart.png')
        plot_bar_chart(employee_attendance_df.set_index('Employee ID'), 'Employee Attendance', 'Employee ID', 'Days Present', 'attendance_chart.png')
        plot_bar_chart(tasks_summary_df.set_index('Status'), 'Tasks Summary', 'Status', 'Count', 'tasks_chart.png')
        plot_bar_chart(finance_summary_df.set_index('Category'), 'Finance Summary', 'Category', 'Amount', 'finance_chart.png')
        plot_pie_chart(finance_summary_df.set_index('Category'), 'Finance Distribution', 'finance_pie_chart.png')

        # Display Summary
        print(f"Total Students: {total_students}")
        print(f"Total Employees: {total_employees}")
        print(f"Total Tasks: {total_tasks}")
        print(f"Average Length of Stay: {avg_length_of_stay:.2f} days")

        print("Finance Summary:")
        for category, amount in finance_summary:
            print(f"{category}: {amount}")

        print("Overdue Tasks:")
        for task in overdue_tasks:
            print(f"- {task[0]}")

        print("Overdue Payments:")
        for payment in overdue_payments:
            print(f"- {payment[0]}")

        print("Pending Maintenance Requests:")
        for maintenance in pending_maintenance_requests:
            print(f"- {maintenance[0]}")

        print("User Feedback:")
        for feedback in user_feedback:
            print(f"- {feedback[0]}")

        main.main()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dashboard()
