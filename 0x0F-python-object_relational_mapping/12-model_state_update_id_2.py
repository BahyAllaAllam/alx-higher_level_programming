#!/usr/bin/python3
'''
script that changes the name of a State object from the database hbtn_0e_6_usa
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

        # Query and update the State object with id=2
        state_to_update = session.query(State).filter_by(id=2).first()
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
            print("State name updated successfully.")
        else:
            print("State with id=2 not found.")

        # Close session
        session.close()
