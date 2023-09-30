from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from config.db_config import *
from sqlalchemy.orm import Session
from .authRouter import current_user
from models.friends import Friends
from schemas.userSchema import UserId

router = APIRouter(prefix="/friends",
                    tags=["friends"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/add/", status_code=status.HTTP_200_OK)
async def postAddFriend(id_friend: UserId, user: User = Depends(current_user), db: Session = Depends(get_db)):
    friend = db.query(User).filter(User.id == id_friend.id_friend).first()
    if friend is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    friend = Friends(
                id_friend = friend.id,
                value = friend.username,
                id_user = user.id
    )
    db.add(friend)
    db.autoflush
    db.commit()
    db.refresh(friend)

    return {"status": status.HTTP_200_OK}

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
def deleteFriendById(id: int, user: UserId = Depends(current_user), db: Session = Depends(get_db)):

    friend = db.query(Friends).filter(Friends.id == id).first()
    
    if friend is None:
        raise HTTPException(status_code=404, detail="Friend not found")
    if friend.id_user != user.id and friend.id_friend != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login first")
    
    db.delete(friend)
    db.commit()
    return {"detail": "Friend deleted successfully"}
