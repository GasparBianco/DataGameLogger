from fastapi import APIRouter, HTTPException, Depends, status, Response
from models.boardgame import UserBoardGameCollection
from schemas.boardGameSchema import *
from config.db_config import *
from sqlalchemy.orm import Session
from .authRouter import current_user
from schemas.userSchema import UserId
from schemas.customResponsesSchemas import *
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/boardgame",
                    tags=["boardGame"],
                    responses={404: {"message": "No encontrado"}})


@router.post("/add/",response_model=BoardGameResponse, responses={
                                    201: {"model": BoardGameResponse},
                                    401: {"model": defaultResponse}
})
async def postBoardGameToCollection(data: BoardGameBase,response: Response, user: UserId = Depends(current_user), db: Session = Depends(get_db)):
    

    new_boardGame = UserBoardGameCollection(
                    id_bgg = data.id_bgg,
                    value = data.value,
                    id_user = user.id
    )
    db.add(new_boardGame)
    db.autoflush
    db.commit()
    db.refresh(new_boardGame)

    response.status_coode = status.HTTP_201_CREATED
    return new_boardGame

@router.delete("/delete/{id}", responses={
                                            200: {"model": defaultResponse},
                                            404: {"model": defaultResponse},
                                            401: {"model": defaultResponse}
})
def deleteBoardGameById(id: int, user: UserId = Depends(current_user), db: Session = Depends(get_db)):

    board_game = db.query(UserBoardGameCollection).filter(UserBoardGameCollection.id == id).first()
    
    if board_game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="BoardGame not found")
    if board_game.id_user != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login first")

    db.delete(board_game)
    db.commit()
    return {"detail": "BoardGame deleted successfully"}
    