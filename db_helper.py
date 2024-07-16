import sqlite3

def execute_query(query, params=()):
    try:
        conn = sqlite3.connect('database/hostel_management.db')
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def fetch_query(query, params=()):
    try:
        conn = sqlite3.connect('database/hostel_management.db')
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
