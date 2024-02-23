#!/usr/bin/python3
"""
To add a new state object to the table states.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    new_state = State(name="Louisiana")
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_state)

    session.commit()

    print("{}".format(new_state.id))
