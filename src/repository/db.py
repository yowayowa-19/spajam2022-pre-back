import psycopg2
from psycopg2 import connection


def connect() -> connection:
    """Connect to the PostgreSQL database. Returns a database connection."""
    return psycopg2.connect("dbname=news")


def create_user():
    pass

def update_user():
    pass
