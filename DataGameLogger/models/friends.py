from sqlalchemy import Column, Integer, String, ForeignKey
from config.db_config import Base
from sqlalchemy.orm import relationship


class Friends(Base):
    __tablename__ = "user_friends"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_friend = Column(Integer, ForeignKey("user.id"), nullable=False)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship('User',
                        back_populates='friends',
                        foreign_keys=[id_user],
                        )
    friend = relationship('User',
                        back_populates='friends',
                        foreign_keys=[id_friend])