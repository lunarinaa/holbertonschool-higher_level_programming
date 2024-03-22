#!/usr/bin/python3
""" database connector"""


import MySQLdb
import sys.argv
if __name__ == "__main__":
    db_connector = MySQLdb.connect(host="localhost", user=argv[1],
                                   passwd=argv[2], db=argv[3], port=3306)
    cursor = db_connector.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
                   "INNER JOIN states ON cities.state_id = states.id"
                   "ORDER BY cities.id")
    output = cursor.fetchall()
    for i in output:
        print(i)
    cursor.close()
