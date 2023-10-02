from pydantic import BaseModel, Field, constr
from typing import List, Optional
from .boardGameSchema import BoardGameResponse


class UserBase(BaseModel):
    username: str = Field(
                            min_length=3,
                            max_length=64,
)

    class Config():
        from_attributes = True

class UserId(BaseModel):
    id: int

class UserLogin(UserBase):
    password: str = Field(
                        max_length=64,
                        min_length=8
    )

class UserRegister(UserLogin):
    email: str = Field(
                        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

class UserResponse(UserBase):
    pass

class UserCollection(UserResponse):
    collection: List[BoardGameResponse]

class UserFriends(BaseModel):
    friends: List[UserResponse]