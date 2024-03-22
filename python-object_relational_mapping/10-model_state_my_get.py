#!/usr/bin/python3
"""script """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = 0
    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = 1
    if found == 0:
        print("Not found")
    session.close()
