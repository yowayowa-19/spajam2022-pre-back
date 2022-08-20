from pydantic import BaseModel

class Credential(BaseModel):
    email: str
    user_name: str
    password: str


class User(BaseModel):
    user_id: int
    region: str
    has_vehicles: bool
    has_aircon: bool
    has_tv: bool