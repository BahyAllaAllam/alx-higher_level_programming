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
        print('Usage: python 0-select_states.py'
              '<username> <password> <database> <state_name>')
        sys.exit(1)

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

        cur = db.cursor()
        query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' ").format(
                 argv[4])
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)
    finally:
        if db:
            db.close()
