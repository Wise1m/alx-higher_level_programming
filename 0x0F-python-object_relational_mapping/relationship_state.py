#!/usr/bin/python3
"""
To create a class that interacts with sql table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state for a Mysql database.

    __tablename__(str): The name of the MySQL table to States.
    if (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="all, delete-orphan", backref="state"
            )
