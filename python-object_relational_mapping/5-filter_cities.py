#!/usr/bin/python3
"""connecting databases"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", user=argv[1],
                                    passwd=argv[2], db=argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute(
                    "SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id",
                    (argv[4],)
                   )
    output = cursor.fetchall()
    cities_for_state = [city[0] for city in output]
    print(", ".join(cities_for_state))
    cursor.close()
