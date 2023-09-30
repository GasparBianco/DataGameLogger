from sqlalchemy import Column, Integer, String
from config.db_config import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    collection = relationship('UserBoardGameCollection',
                            back_populates="user", 
                            cascade="all, delete-orphan")
    friends = relationship('Friends',
                        back_populates='user',
                        foreign_keys='Friends.id_user',
                        )