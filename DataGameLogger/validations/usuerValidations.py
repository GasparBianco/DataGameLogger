from schemas.userSchema import UserRegister
from fastapi import HTTPException, status
import re
from models.user import User

def emailValidator(email):
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        return True
    else:
        return False
    
def  userRegisterValidations(user_data: UserRegister, db):
    if 3 > len(user_data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username too short")
    if 8 > len(user_data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password too short")
    if not user_data.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email can not by empty")
    if not emailValidator(user_data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exist")
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")
