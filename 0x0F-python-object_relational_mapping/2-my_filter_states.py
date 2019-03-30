#!/usr/bin/python3
"""display matching arguments"""
import MySQLdb
import sqlalchemy
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE `name` = '{}' ORDER
    BY `states`.`id` ASC""".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        print(state)
    c.close()
    db.close()
