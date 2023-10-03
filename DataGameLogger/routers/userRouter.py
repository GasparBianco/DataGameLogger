from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from schemas.userSchema import *
from config.db_config import *
from sqlalchemy.orm import Session
from validations.userValidations import userRegisterValidations
from .authRouter import current_user
from models.friends import Friends
from schemas.customResponsesSchemas import *
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/user",
                    tags=["user"],
                    responses={404: {"message": "No encontrado"}})

@router.get("/collection/",response_model=UserCollection, responses={
                                        200: {"model": UserCollection},
                                        404: {"model": defaultResponse},
                                        401: {"model": defaultResponse}
})
async def getUserCollection(user: User = Depends(current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user.id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.get("/friends/",response_model=UserFriends, responses={
                                        200: {"model": UserFriends},
                                        404: {"model": defaultResponse},
                                        401: {"model": defaultResponse}
})
async def getUserFriends(user: UserId = Depends(current_user), db: Session = Depends(get_db)):
    user_list = db.query(Friends).filter(Friends.id_user == user.id).all()
    id_list = [friend.id_friend for friend in user_list]
    user_list.extend(db.query(Friends).filter(Friends.id_friend == user.id).all())
    id_list.extend([friend.id_user for friend in user_list])
    id_list = [x for x in id_list if x != user.id]
    friends_list = db.query(User).filter(User.id.in_(id_list)).all()
    
    return {"friends": friends_list}

