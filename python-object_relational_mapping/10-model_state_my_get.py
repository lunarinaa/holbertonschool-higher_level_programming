#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.crreate_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    met = 0
    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            met = 1
    if met == 0:
       print("Not found")
    session.close()
