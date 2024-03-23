#!/usr/bin/python3
"""prints all City objects from the database"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State, City).join(City).order_by(City.id):
        print("{:}: ({:}) {:}".format(row[0].name, row[1].id, row[1].name))
    session.commit()
    session.close()
