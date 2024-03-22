#!/usr/bin/python3
""" establishing database connection"""


import MySQLdb
import sys

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
      host="localhost", user=sys.argv[1],
      passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute(
      "SELECT cities.id, cities.name, states.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    )
    output = cursor.fetchall()
    for i in output:
        print(i)
    cursor.close()
