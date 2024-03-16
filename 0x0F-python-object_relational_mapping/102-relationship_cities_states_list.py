#!/usr/bin/python3
'''
script that lists all City objects from the database hbtn_0e_101_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City


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

        # Query all City objects with their corresponding State objects
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

        # Close session
        session.close()
