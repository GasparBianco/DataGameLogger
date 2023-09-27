from pydantic import BaseModel
from typing import List, Optional

class BoardGameBase(BaseModel):
    value: str
    id_bgg: int

class BoardGame(BoardGameBase):

    id_user: int