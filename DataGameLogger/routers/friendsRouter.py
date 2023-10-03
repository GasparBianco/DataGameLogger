from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from config.db_config import *
from sqlalchemy.orm import Session
from .authRouter import current_user
from models.friends import Friends
from schemas.userSchema import UserId
from schemas.customResponsesSchemas import *
from fastapi.responses import JSONResponse
from sqlalchemy import and_

router = APIRouter(prefix="/friends",
                    tags=["friends"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/add/", responses={
                                    201: {"model": defaultResponse},
                                    404: {"model": defaultResponse},
})
async def postAddFriend(id_friend: int, user: User = Depends(current_user), db: Session = Depends(get_db)):
    friend = db.query(User).filter(User.id == id_friend).first()
    if friend is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = Friends(
                id_friend = friend.id,
                id_user = user.id
    )
    db.add(friend)
    db.autoflush
    db.commit()
    db.refresh(friend)
    
    response = {"detail": "Friend added successfully"}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)

@router.delete("/delete/{id_friend}", responses={
                                            200: {"model": defaultResponse},
                                            404: {"model": defaultResponse},
                                            401: {"model": defaultResponse}
})
def deleteFriendById(id_friend: int, user: UserId = Depends(current_user), db: Session = Depends(get_db)):

    friend = db.query(Friends).filter(and_(Friends.id_friend == user.id, Friends.id_user == id_friend)).first()    
    if friend is None:
        friend = db.query(Friends).filter(and_(Friends.id_user == user.id, Friends.id_friend == id_friend)).first()
    if friend is None:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    db.delete(friend)
    db.commit()
    return {"detail": "Friend deleted successfully"}
    