#!/usr/bin/python3
'''
script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
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

        # Query and delete State objects with a name containing the letter 'a'
        states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()
        for state in states_to_delete:
            session.delete(state)

        session.commit()
        print("States with names containing 'a' deleted successfully.")

        # Close session
        session.close()
