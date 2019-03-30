#!/usr/bin/python3
"""list all state database obj's from hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sys

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.close()
