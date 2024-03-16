#!/usr/bin/python3
"""Module for defining State class and Base instance."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """State class representing the 'states' table in the database."""

    __tablename__ = 'states'

    id = Column(
        Integer,
        unique=True,
        primary_key=True,
        nullable=False,
        autoincrement=True)

    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        backref=backref("state", cascade="all"),
        cascade="all, delete-orphan",
        single_parent=True)
