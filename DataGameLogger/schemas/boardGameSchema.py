from pydantic import BaseModel
from typing import List, Optional

class BoardGameBase(BaseModel):    
    value: str
    id_bgg: int

    class Config():
        from_attributes = True

class BoardGameCreate(BoardGameBase):

    id_user: int


class BoardGameResponse(BoardGameBase):
    id: int