import sqlite3
import os

def connect_db():
    # Construct the path to the database file
    db_path = os.path.join(os.path.dirname(__file__), 'data', 'hostel_management.db')
    conn = sqlite3.connect(db_path)
    return conn

def execute_query(query, params=()):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def fetch_query(query, params=()):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
