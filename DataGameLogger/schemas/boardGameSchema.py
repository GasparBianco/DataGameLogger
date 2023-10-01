from pydantic import BaseModel
from typing import List, Optional

class BoardGameBase(BaseModel):    
    value: str
    id_bgg: int

    class Config():
        from_attributes = True

class BoardGameResponse(BoardGameBase):
    id: int