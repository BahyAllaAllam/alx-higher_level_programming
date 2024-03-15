#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states
from a specified database whose names start with 'N'.
"""

import MySQLdb
import sys


def list_states_with_n(username, password, database):
    """
    Connects to the MySQL server and lists states whose names start with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database)
        cursor = conn.cursor()

        # Execute the query to select states starting with 'N'
        cursor.execute("SELECT id, name FROM states WHERE name\
                       LIKE 'N%' ORDER BY id ASC")

        # Fetch all rows and display them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: python 1-filter_states.py '
              '<username> <password> <database>')
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_n(username, password, database)
