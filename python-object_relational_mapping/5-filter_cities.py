#!/usr/bin/python3
"""connecting databases"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", user=argv[1],
                                    passwd=argv[2], db=argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    WHERE state_id = (SELECT id \
                    FROM states WHERE name = '{}')".format(sys.argv[4]))
    # output = cursor.fetchall()
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db_connection.close()
