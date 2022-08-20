import psycopg2
from psycopg2 import connection, cursor

from types import Credential


def connect() -> connection:
    # TODO read from config
    username = "yowayowa"
    hostname = "postgres"
    port = 5432
    database = "pg"

    with open("/run/secrets/POSTGRES_PASSWORD", "r") as f:
        password = f.read()

    conn = psycopg2.connect(
        f"postgresql://{username}:{password}@{hostname}:{port}/{database}"
    )
    return conn


def create_user(credential: Credential):
    with connect() as conn, conn.cursor as cur:
        cur: cursor
        cur.execute("SELECT * FROM users WHERE email = %s", (credential.email,))
        if cur.rowcount == 0:
            cur.execute(
                "INSERT INTO users (name, email, region) VALUES (%s, %s, %s)",
                (credential.user_name, credential.email, credential.region),
            )
            conn.commit()
            return cur.fetchone()[0]
        else:
            return 0


def update_user():
    pass
