#!/usr/bin/python3
'''
the class definition of a City
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''the class definition of a City'''

    __tablename__ = 'cities'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        primary_key=True,
        autoincrement=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
