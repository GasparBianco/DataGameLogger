from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from config.db_config import *
from sqlalchemy.orm import Session
from .authRouter import current_user
from models.friends import Friends
from schemas.userSchema import UserId
from schemas.customResponsesSchemas import *
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/friends",
                    tags=["friends"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/add/", responses={
                                    201: {"model": defaultResponse},
                                    404: {"model": defaultResponse},
})
async def postAddFriend(id_friend: UserId, user: User = Depends(current_user), db: Session = Depends(get_db)):
    friend = db.query(User).filter(User.id == id_friend.id).first()
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

@router.delete("/delete/{id}", responses={
                                            200: {"model": defaultResponse},
                                            404: {"model": defaultResponse}
})
def deleteFriendById(id: int, user: UserId = Depends(current_user), db: Session = Depends(get_db)):

    friend = db.query(Friends).filter(Friends.id == id).first()
    
    if friend is None:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    db.delete(friend)
    db.commit()
    return {"detail": "Friend deleted successfully"}
    