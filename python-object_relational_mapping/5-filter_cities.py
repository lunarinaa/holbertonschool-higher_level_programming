#!/usr/bin/python3
"""
Lists all cities of a given state from the states table of hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Connect to the database
        db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        # Create a cursor object
        cursor = db_connection.cursor()

        # Execute SQL query
        cursor.execute(
            """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """,
            (sys.argv[4],)
        )

        # Fetch all rows
        output = cursor.fetchall()

        # Print cities for the specified state
        cities_for_state = [city[0] for city in output]
        print(", ".join(cities_for_state))

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close cursor and database connection
        cursor.close()
        db_connection.close()

