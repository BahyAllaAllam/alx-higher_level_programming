#!/usr/bin/python3
'''
script that lists all cities from the database hbtn_0e_4_usa
'''
import MySQLdb
import sys


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print('Usage: python script_name.py'
              'mysql_username mysql_password database_name')
    else:
        # Extract command-line arguments
        username, password, database = sys.argv[1:]

        try:
            db = MySQLdb.connect(host="localhost", port=3306, user=username,
                                 passwd=password, db=database)

            cur = db.cursor()
            query = "SELECT cities.id, cities.name, states.name FROM cities " +
                     "JOIN states ON cities.state_id = states.id " +
                     "ORDER BY cities.id ASC;"
            cur.execute(query)

            rows = cur.fetchall()
            for row in rows:
                print(row)

            cur.close()
            db.close()

        except MySQLdb.Error as e:
            print("Error:", e)
