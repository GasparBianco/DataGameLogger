from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from schemas.userSchema import *
from config.db_config import *
from sqlalchemy.orm import Session



router = APIRouter(prefix="/user",
                    tags=["user"],
                    responses={404: {"message": "No encontrado"}})

