#!/usr/bin/python3
"""list all states starting w/ uppercase N"""
import MySQLdb
import sqlalchemy
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    c=db.cursor()
    c.execute("""SELECT * FROM states WHERE ASCII(name)=ASCII('N')
    ORDER BY 'states.id' ASC""")
    states = c.fetchall()
    for state in states:
        print("", state)
    c.close()
    db.close()
