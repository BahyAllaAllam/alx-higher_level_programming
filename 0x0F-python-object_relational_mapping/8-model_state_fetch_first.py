#!/usr/bin/python3
'''
script that prints the first State object from the database hbtn_0e_6_usa
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

        # Fetch the first State object and print it
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print(f'{first_state.id}: {first_state.name}')
        else:
            print('Nothing')

        # Close session
        session.close()
