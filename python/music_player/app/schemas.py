from pydantic import BaseModel
from typing import List


#Schemas users
class User(BaseModel):
    username: str
    full_name: str
    email: str
    role: str
    type_license: str
    disabled: bool


class UserPass(User):
    password: str