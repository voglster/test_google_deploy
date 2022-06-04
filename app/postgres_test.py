import psycopg2
from psycopg2 import Error
from os import getenv

from contextlib import contextmanager


@contextmanager
def get_cursor():
    host = getenv("PG_HOST")
    connection = psycopg2.connect(
        user="postgres", password="test", host=host, port="45432", database="postgres"
    )
    cursor = None
    try:
        cursor = connection.cursor()
        yield connection, cursor

    except (Exception, Error) as error:
        print(f"Error while connecting to PostgreSQL {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def connect():
    with get_cursor() as (conn, cur):
        print(conn.get_dsn_parameters(), "\n")
        print("PostgreSQL server information")
        cur.execute("SELECT version();")
        record = cur.fetchone()
        return f"You are connected to - {record}"


def get_data():
    with get_cursor() as (conn, cur):
        sql = "SELECT * FROM hdd_by_state LIMIT 100"
        cur.execute(sql)
        return cur.fetchall()
