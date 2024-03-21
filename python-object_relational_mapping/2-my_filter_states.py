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
     "SELECT * FROM states WHERE name LIKE '{}' "
     "ORDER BY id".format(sys.argv[4])
    )
    output = cursor.fetchall()
    for i in output:
        print(i)
    cursor.close()
