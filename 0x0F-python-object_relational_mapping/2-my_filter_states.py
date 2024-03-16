#!/usr/bin/python3
"""
This script connects to a MySQL server and
    displays all values in the states table
where the name matches the provided argument.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to the MySQL server and filters states by the provided name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database)
        cursor = conn.cursor()

        # Create and execute the SQL query using format with user input
        query = ("SELECT * FROM states WHERE name = '{}' "
                 "ORDER BY id ASC;").format(state_name)
        cursor.execute(query)

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
    if len(sys.argv) != 5:
        print("Usage: python 2-my_filter_states.py "
              "<username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    filter_states(username, password, database, state_name)
