from sqlalchemy import Column, Integer, String, ForeignKey
from config.db_config import Base



class UserBoardGameCollection(Base):
    __tablename__ = "user_boardgame_collection"
    id = Column(Integer, primary_key=True, index=True)
    id_bgg = Column(Integer)
    value = Column(String(255))
    id_user = Column(Integer, ForeignKey("user.id"), primary_key=True)