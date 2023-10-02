from schemas.userSchema import UserRegister
from fastapi import HTTPException, status
import re
from models.user import User
from config.auth_config import crypt
    
def  userRegisterValidations(user_data: UserRegister, db):
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exist")
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")

def loginValidations(form, db):
    user = db.query(User).filter(User.username == form.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username incorrect")
    if not crypt.verify(form.password, user.password):        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password incorrect")