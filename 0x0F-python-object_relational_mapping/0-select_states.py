#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states
    from a specified database.
"""

import MySQLdb
import sys


if __name__ == '__main__':

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print('Usage: python 0-select_states.py'
              '<username> <password> <database>')
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)

        cur = db.cursor()
        cur.execute("SELECT * FROM states")

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)
    finally:
        if db:
            db.close()
