from sqlalchemy import Column, Integer, String, ForeignKey
from .db_config import Base
from sqlalchemy.orm import relationship


class UserBoardGameCollection(Base):
    __tablename__ = "user_boardgame_collection"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_bgg = Column(Integer, nullable=True)
    value = Column(String(255), nullable=False)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates= "collection")