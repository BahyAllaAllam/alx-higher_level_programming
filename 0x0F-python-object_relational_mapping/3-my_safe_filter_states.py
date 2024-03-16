#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states
    from a specified database.
"""

import MySQLdb
import sys


if __name__ == '__main__':

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print('Usage: python script_name.py mysql_username mysql_password '
              'database_name state_name')
    else:
        # Extract command-line arguments
        username, password, database, state_name = sys.argv[1:]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
