from dataclasses import dataclass
from typing import Literal
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


@dataclass
class Mission:
    mission_id: int
    title: str
    describe: str
    point: int
    status: bool


def get_missions(user_id: int, type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        cur.execute(
            """
        SELECT 
            mission.id, 
            mission.title, 
            mission.describe, 
            mission.point, 
            history.current_point,
            history.completed_at
        FROM %s AS history
        INNER JOIN %s AS mission
        ON %s.mission_id = %s.id
        WHERE history.user_id = %s
        """,
            (
                type + "_history_table",
                type + "_mission_table",
                type + "_history_table",
                type + "_mission_table",
                user_id,
            ),
        )
        missions: list[Mission] = [
            Mission(
                mission_id=item[0],
                title=item[1],
                describe=item[2],
                point=item[4],
                status=item[3] == item[4] or item[5] is not None,
            )
            for item in cur.fetchall()
        ]
        return missions


def complete_mission():
    with connect() as conn, conn.cursor() as cur:
        cur.execute()


def create_missions(type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM user_table")
        user_ids: list[int] = [item[0] for item in cur.fetchall()]
        cur.execute("SELECT id FROM %s", (type + "_mission_table",))
        missions: list[int] = [item[0] for item in cur.fetchall()]
        for user_id in user_ids:
            for mission_id in missions:
                cur.execute(
                    "INSERT INTO %s (user_id, mission_id) VALUES (%s, %s)",
                    (type + "_history_table", user_id, mission_id),
                )
        conn.commit()


def delete_missions(type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM %s", (type + "_mission_table",))
