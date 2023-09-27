from pydantic import BaseModel
from typing import List, Optional

class BoardGameBase(BaseModel):
    id : int
    value: str
    id_bgg: int

    class Config():
        from_attributes = True

class BoardGame(BoardGameBase):

    id_user: int