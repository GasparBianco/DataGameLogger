from sqlalchemy import Column, Integer, String
from config.db_config import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))
    collection = relationship('UserBoardGameCollection', backref='collection', cascade="all, delete-orphan")