#!/usr/bin/python3
'''
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print('Usage: python script_name.py mysql_username '
              'mysql_password database_name')
    else:
        # Extract command-line arguments
        username, password, database = sys.argv[1:]

        # Create engine and bind session
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Add State object "Louisiana" to the database
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()

        # Print the new states.id after creation
        print(louisiana.id)

        # Close session
        session.close()
