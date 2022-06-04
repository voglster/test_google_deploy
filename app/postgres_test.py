import psycopg2
from psycopg2 import Error
from os import getenv

def connect():
    try:
        # Connect to an existing database
        host = getenv('PG_HOST')
        connection = psycopg2.connect(user="postgres",
                                      password="test",
                                      host=host,
                                      port="45432",
                                      database="postgres")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        return f"You are connected to - {record}"

    except (Exception, Error) as error:
        return f"Error while connecting to PostgreSQL {error}"
    finally:
        if (connection):
            cursor.close()
            connection.close()
