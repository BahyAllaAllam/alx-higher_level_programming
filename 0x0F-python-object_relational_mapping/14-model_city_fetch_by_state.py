#!/usr/bin/python3
'''
prints all City objects from the database hbtn_0e_14_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database)
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all City objects and their respective state names
        cities = session.query(State, City).join(City).order_by(City.id)

        # Print the results in the specified format
        for state, city in cities:
            print(
                "{}: ({}) {}".format(state.name, city.id, city.name)
            )

        # Close session
        session.close()
