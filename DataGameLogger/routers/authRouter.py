from fastapi import APIRouter, Depends, HTTPException, status, Response
from jose import JWTError, jwt
from datetime import datetime, timedelta
from config.db_config import *
from sqlalchemy.orm import Session
from validations.userValidations import loginValidations, userRegisterValidations
from schemas.userSchema import *
from models.user import User
from config.auth_config import *
from schemas.customResponsesSchemas import *
from fastapi.responses import JSONResponse



router = APIRouter(prefix="/auth",
                    tags=["auth"],
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})



async def auth_user(db: Session = Depends(get_db), token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return db.query(User).filter(User.username == username).first()


async def current_user(user: User = Depends(auth_user)):
    return user


@router.post("/login/",responses={
                                    400: {"model": defaultResponse},
                                    200: {"model": AuthTokenResponse}
})
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    loginValidations(form, db)

    access_token = {
                    "sub": form.username,
                    "exp": datetime.utcnow() + timedelta(weeks=ACCESS_TOKEN_DURATION)}
    
    response = {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
                "token_type": "bearer"}
    
    return response


@router.post("/register/",response_model=UserResponse, responses={
                                        400: {"model": defaultResponse},
                                        201: {"model": UserResponse}
})
async def registerUser(user_data: UserRegister, response: Response, db: Session = Depends(get_db)):
    
    userRegisterValidations(user_data, db)

    password = crypt.encrypt(user_data.password)
    
    new_user = User(
                    username = user_data.username,
                    email = user_data.email,
                    password = password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    response.status_code = status.HTTP_201_CREATED
    return new_user
