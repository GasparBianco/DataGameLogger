from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(UserLogin):
    email: str
