from contextlib import contextmanager
import datetime
from decimal import Decimal
from urllib.parse import urlparse
import psycopg2, os
from psycopg2.extras import register_inet, Inet
from psycopg2.pool import ThreadedConnectionPool



DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

url = urlparse(DATABASE_URL)
pool = ThreadedConnectionPool(1, 20,
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port)


@contextmanager
def get_db_connection():
    """
    psycopg2 connection context manager.
    Fetch a connection from the connection pool and release it.
    """
    try:
        connection = pool.getconn()
        yield connection
    finally:
        pool.putconn(connection)


@contextmanager
def get_db_cursor(commit=False):
    """
    psycopg2 connection.cursor context manager.
    Creates a new cursor and closes it, commiting changes if specified.
    """
    with get_db_connection() as connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield cursor
            if commit:
                connection.commit()
        finally:
            cursor.close()
