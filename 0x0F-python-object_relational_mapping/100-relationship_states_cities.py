#!/usr/bin/python3
'''
script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create the State "California" with the City "San Francisco"
        california = State(name="California")
        san_francisco = City(name="San Francisco", state=california)
        session.add(california)
        session.add(san_francisco)
        session.commit()

        print("State 'California' with City 'San Francisco' "
              "created successfully.")

        # Close session
        session.close()
