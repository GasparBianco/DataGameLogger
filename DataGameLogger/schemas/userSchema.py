from pydantic import BaseModel
from typing import List, Optional
from .boardGameSchema import BoardGameBase

class UserBase(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(UserLogin):
    email: str

class UserCollection(BaseModel):
    collection: List[BoardGameBase]