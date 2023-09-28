from schemas.userSchema import UserRegister
from fastapi import HTTPException, status
import re
from models.user import User
from config.auth_config import crypt

def emailValidator(email):
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        return True
    else:
        return False
    
def passwordValidator(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#$!%^&*]{8,}$'
    
    if re.match(patron, password):
        return True
    else:
        return False
    
def  userRegisterValidations(user_data: UserRegister, db):
    if 3 > len(user_data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username too short")
    if 6 > len(user_data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")
    if not user_data.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email can not by empty")
    if not emailValidator(user_data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
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