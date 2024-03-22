#!/usr/bin/python3
"""connecting databases"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", user=argv[1],
                                    passwd=argv[2], db=argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argv[4], ))
    print(", ".join(map(lambda x: x[0], cursor.fetchall())))
    cursor.close()
