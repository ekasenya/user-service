from pydantic import BaseModel
from typing import Optional


class UserInfo(BaseModel):
    name: str
    email: Optional[str]


class User(BaseModel):
    user_id: int
    user_info: UserInfo
