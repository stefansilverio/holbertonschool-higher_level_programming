#!/usr/bin/python3
"""print all city obj's from hbtn_0e_14_usa"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sys

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(City, State.name).join(State).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(s[1], s[0].id, s[0].name))
    session.close()
