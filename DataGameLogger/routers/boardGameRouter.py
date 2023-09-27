from fastapi import APIRouter, HTTPException, Depends, status
from models.boardgame import UserBoardGameCollection
from schemas.boardGameSchema import *
from config.db_config import *
from sqlalchemy.orm import Session



router = APIRouter(prefix="/boardgame",
                    tags=["boardGame"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/add/", response_model=BoardGame, status_code=status.HTTP_201_CREATED)
async def addBoardGameToCollection(data: BoardGame, db: Session = Depends(get_db)):
    
    new_boardGame = UserBoardGameCollection(
                    id_bgg = data.id_bgg,
                    value = data.value,
                    id_user = data.id_user
    )
    db.add(new_boardGame)
    db.autoflush
    db.commit()
    db.refresh(new_boardGame)
    return new_boardGame
