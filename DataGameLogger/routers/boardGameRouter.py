from fastapi import APIRouter, HTTPException, Depends, status
from models.boardgame import UserBoardGameCollection
from schemas.boardGameSchema import *
from config.db_config import *
from sqlalchemy.orm import Session
from .authRouter import current_user
from schemas.userSchema import UserId


router = APIRouter(prefix="/boardgame",
                    tags=["boardGame"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/add/", response_model=BoardGameResponse, status_code=status.HTTP_201_CREATED)
async def postBoardGameToCollection(data: BoardGameCreate, db: Session = Depends(get_db)):
    
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

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
def deleteBoardGameById(id: int, user: UserId = Depends(current_user), db: Session = Depends(get_db)):

    board_game = db.query(UserBoardGameCollection).filter(UserBoardGameCollection.id == id).first()
    
    if board_game is None:
        raise HTTPException(status_code=404, detail="BoardGame not found")
    if board_game.id_user != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login first")

    db.delete(board_game)
    db.commit()
    return {"detail": "BoardGame deleted successfully"}