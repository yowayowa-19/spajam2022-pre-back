import psycopg2


class Credential:
    email: str
    user_name: str
    password: str


class User:
    user_id: int
    region: str
    has_vehicles: bool
    has_aircon: bool
    has_tv: bool
    annotation: str

    class Config:
        orm_mode = True


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
        cur.execute("SELECT * FROM user_table WHERE name = %s", (credential.user_name,))
        if cur.rowcount == 0:
            cur.execute(
                "INSERT INTO user_table (name, password) VALUES (%s, %s)",
                (credential.user_name, credential.password),
            )
            conn.commit()
            return True
        else:
            return False


def update_user_profile(user: User):
    conn = connect() 
    with connect() as conn, conn.cursor() as cur:
        cur.execute(
            "UPDATE user_table SET has_car = %s, has_aircon = %s, has_tv = %s\
                WHERE id = %s",
            (user.has_vehicles, user.has_aircon, user.has_tv, user.user_id))
        conn.commit()
        return True


def password_check_user(credential: Credential):
    conn = connect()
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT id,password FROM user_table WHERE name = %s",
            (credential.user_name,))
        if cur.rowcount == 0:
            return 0
        elif cur.rowcount >= 2:
            return 0
        else:
            res = cur.fetchall()
            if res[0][1] == credential.password:
                return res[0][0]
            else:
                return 0

  
