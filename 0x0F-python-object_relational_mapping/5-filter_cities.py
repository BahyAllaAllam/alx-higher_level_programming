#!/usr/bin/python3
'''
script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''

import MySQLdb
import sys


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print('Usage: python script_name.py mysql_username '
              'mysql_password database_name state_name')
    else:
        # Extract command-line arguments
        username, password, database, state_name = sys.argv[1:]

        try:
            db = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)

            cur = db.cursor()
            query = "SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s ORDER BY cities.id ASC"
            cur.execute(query, (state_name,))

            row = cur.fetchone()
            if row:
                print(row[0])
            else:
                print(f"No cities found for state '{state_name}'")

            cur.close()
            db.close()

        except MySQLdb.Error as e:
            print("Error:", e)
