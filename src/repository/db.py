from dataclasses import dataclass
from typing import Literal
import psycopg2


@dataclass
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


def get_user_info(user_id: int):
    conn = connect()
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT name, total_points FROM user_table WHERE id = %s", (user_id,))
        res = cur.fetchone()
        user_info = {"user_name": res[0], "total_points": res[1]}
        
        return user_info


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
            (user.has_vehicles, user.has_aircon, user.has_tv, user.user_id,))
        conn.commit()
        cur.execute(
                "SELECT id, region, has_car, has_aircon, has_tv FROM user_table WHERE id = %s",
                (user.user_id,))
        result = cur.fetchone()
        user.user_id = result[0]
        user.region = result[1]
        user.has_vehicles = result[2]
        user.has_aircon = result[3]
        user.has_tv = result[4]
        return user

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

  
def update_user():
    pass


# @dataclass
# class Mission:
#     mission_id: int
#     title: str
#     describe: str
#     point: int
#     cuurent_point: int
#     status: bool


def get_missions(user_id: int, type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        if type == "daily":
            cur.execute(
                """
            SELECT 
                mission.id, 
                mission.title, 
                mission.describe, 
                mission.point, 
                history.current_point,
                history.completed_at
            FROM daily_history_table AS history
            INNER JOIN daily_mission_table AS mission
            ON history.mission_id = mission.id
            WHERE history.user_id = %s
            """,
                (user_id,),
            )
        else:
            cur.execute(
                """
            SELECT 
                mission.id, 
                mission.title, 
                mission.describe, 
                mission.point, 
                history.current_point,
                history.completed_at
            FROM weekly_history_table AS history
            INNER JOIN weekly_mission_table AS mission
            ON history.mission_id = mission.id
            WHERE history.user_id = %s
            """,
                (user_id,),
            )

        result = cur.fetchall()

        missions: list[dict] = [
            {
                "mission_id": item[0],
                "title": item[1],
                "describe": item[2],
                "point": item[3],
                "current_point": item[4],
                "status": item[3] == item[4] or item[5] is not None,
            }
            for item in result
        ]
        return missions


@dataclass
class DoneMission:
    user_id: int
    mission_id: int
    type: Literal["daily", "weekly"]
    point: int


def update_mission(args: DoneMission):
    with connect() as conn, conn.cursor() as cur:
        # daily | weekly
        # update daily_mission_table or weekly_mission_table

        # get previeous point
        if args.type == "daily":
            cur.execute(
                "SELECT current_point FROM daily_history_table WHERE user_id = %s AND mission_id = %s",
                (args.user_id, args.mission_id),
            )
        else:
            cur.execute(
                "SELECT current_point FROM weekly_history_table WHERE user_id = %s AND mission_id = %s",
                (args.user_id, args.mission_id),
            )
        previouts_point = cur.fetchone()[0]

        if args.type == "daily":
            cur.execute(
                "UPDATE daily_history_table SET current_point = %s WHERE user_id = %s AND mission_id = %s",
                (args.point, args.user_id, args.mission_id),
            )
        else:
            cur.execute(
                "UPDATE weekly_history_table SET current_point = %s WHERE user_id = %s AND mission_id = %s",
                (args.point, args.user_id, args.mission_id),
            )

        # get current_point
        if args.type == "daily":
            cur.execute(
                "SELECT current_point FROM daily_history_table WHERE user_id = %s AND mission_id = %s",
                (args.user_id, args.mission_id),
            )
        else:
            cur.execute(
                "SELECT current_point FROM weekly_history_table WHERE user_id = %s AND mission_id = %s",
                (args.user_id, args.mission_id),
            )
        current_point = cur.fetchone()[0]

        # update user status
        cur.execute(
            "UPDATE user_table SET total_points = total_points + %s WHERE id = %s",
            (current_point - previouts_point, args.user_id),
        )

        # return user data
        cur.execute("SELECT id, region, has_car, has_aircon, has_tv, total_points FROM user_table WHERE id = %s", (args.user_id,))
        user = cur.fetchone()
        return {
            "user_id": user[0],
            "region": user[1],
            "has_vehicles": user[2],
            "has_aircon": user[3],
            "has_tv": user[4],
            "total_point": user[5],
        }


def create_missions(type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM user_table")
        user_ids: list[int] = [item[0] for item in cur.fetchall()]
        if type == "daily":
            cur.execute("SELECT id FROM daily_mission_table")
        else:
            cur.execute("SELECT id FROM weekly_mission_table")
        missions: list[int] = [item[0] for item in cur.fetchall()]
        for user_id in user_ids:
            for mission_id in missions:
                if type == "daily":
                    cur.execute(
                        "INSERT INTO daily_history_table (user_id, mission_id) VALUES (%s, %s)",
                        (user_id, mission_id),
                    )
                else:
                    cur.execute(
                        "INSERT INTO weekly_history_table (user_id, mission_id) VALUES (%s, %s)",
                        (user_id, mission_id),
                    )
        conn.commit()
        # cur.execute("SELECT * FROM daily_history_table")
        # print(cur.fetchall())


def delete_missions(type: Literal["daily", "weekly"]):
    with connect() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM %s", (type + "_mission_table",))
