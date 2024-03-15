#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states
    from a specified database.

Usage:
    python 0-select_states.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Database name

Example:
    python 0-select_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to the MySQL server and lists all states
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        conn = MySQLdb.connect(
                host='localhost', port=3306, user=username,
                     passwd=password, db=database
        )
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

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
        print('Usage: python 0-select_states.py '
              '<username> <password> <database>')
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
