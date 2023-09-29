from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from schemas.userSchema import *
from config.db_config import *
from sqlalchemy.orm import Session
from validations.usuerValidations import userRegisterValidations
from .auth import current_user


router = APIRouter(prefix="/user",
                    tags=["user"],
                    responses={404: {"message": "No encontrado"}})

@router.get("/collection/", response_model=UserCollection, status_code=status.HTTP_200_OK)
async def getIngredientPage(user: User = Depends(current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user.id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
