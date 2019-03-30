#!/usr/bin/python3
"""display matching arguments"""
import MySQLdb
import sqlalchemy
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT `cities`.`name` FROM `cities` INNER JOIN
    `states` ON `cities`.`state_id` = `states`.`id` WHERE
    `states`.`name` = %s ORDER BY cities.id ASC""", (sys.argv[4],))
    cities = c.fetchall()
    count = 0
    for city in cities:
        print(''.join(city), end="")
        count += 1
        if count < len(cities):
            print(", ", end="")
    print()
    c.close()
    db.close()
