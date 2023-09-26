from fastapi import APIRouter, HTTPException, Depends, status
from models.user import User
from schemas.userSchema import *
from config.db_config import *
from sqlalchemy.orm import Session



router = APIRouter(prefix="/user",
                    tags=["user"],
                    responses={404: {"message": "No encontrado"}})

@router.post("/register/", response_model= UserResponse, status_code=status.HTTP_201_CREATED)
async def registerUser(user_data: UserRegister, db: Session = Depends(get_db)):
    
    new_user = User(
                    username = user_data.username,
                    email = user_data.email,
                    password = user_data.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
