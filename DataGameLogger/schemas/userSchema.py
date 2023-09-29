from pydantic import BaseModel
from typing import List, Optional
from .boardGameSchema import BoardGameResponse

class UserBase(BaseModel):
    username: str

    class Config():
        from_attributes = True

class UserLogin(UserBase):
    password: str

class UserRegister(UserLogin):
    email: str

class UserResponse(UserBase):
    id: int

class UserCollection(UserResponse):
    collection: List[BoardGameResponse]