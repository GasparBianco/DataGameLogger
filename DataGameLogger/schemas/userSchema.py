from pydantic import BaseModel
from typing import List, Optional
from .boardGameSchema import BoardGameResponse


class UserBase(BaseModel):
    username: str

    class Config():
        from_attributes = True

class UserId(BaseModel):
    id: int

class UserLogin(UserBase):
    password: str

class UserRegister(UserLogin):
    email: str

class UserResponse(BaseModel):
    id: int
    username: str

class UserCollection(UserResponse):
    collection: List[BoardGameResponse]

class UserFriends(BaseModel):
    friends: List[UserResponse]