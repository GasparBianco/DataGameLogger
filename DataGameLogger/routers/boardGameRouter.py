from fastapi import APIRouter, HTTPException, Depends
from models.boardgame import UserBoardGameCollection
from schemas.userSchema import *
from config.db_config import *
from sqlalchemy.orm import Session



router = APIRouter(prefix="/boardgame",
                    tags=["boardGame"],
                    responses={404: {"message": "No encontrado"}})