#!/usr/bin/python3
'''
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print('Usage: python script_name.py mysql_username '
              'mysql_password database_name state_name')
    else:
        # Extract command-line arguments
        username, password, database, state_name = sys.argv[1:]

        # Create engine and bind session
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Search for State object with the specified name
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print('Not found')

        # Close session
        session.close()
