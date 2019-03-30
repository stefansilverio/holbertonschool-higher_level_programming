#!/usr/bin/python3
"""change name of db object"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
import sqlalchemy
import sys

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.id == 2).first()
    if instance:
        instance.name = "New Mexico"
        session.commit()
    session.close()
