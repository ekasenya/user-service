from typing import Optional

from pydantic import BaseModel


class UserInfo(BaseModel):
    name: str
    email: Optional[str]


class User(BaseModel):
    user_id: int
    user_info: UserInfo
