import psycopg2

class Credential:
    email: str
    user_name: str
    password: str

def connect():
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
    conn = connect()
    with connect() as conn, conn.cursor() as cur:
        # cur: cursor
        cur.execute("SELECT * FROM user_table WHERE email = %s", (credential.email,))
        if cur.rowcount == 0:
            cur.execute(
                "INSERT INTO user_table (name, email) VALUES (%s, %s)",
                (credential.user_name, credential.email),
            )
            conn.commit()
            return True
        else:
            return False


def update_user():
    pass
