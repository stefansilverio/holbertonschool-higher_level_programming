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
    c.execute("""SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
    FROM cities INNER JOIN states ON `cities`.`state_id` = `states`.`id`
    ORDER BY cities.id ASC""")
    cities = c.fetchall()
    for city in cities:
        print(city)
    c.close()
    db.close()
