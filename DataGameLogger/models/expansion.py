from sqlalchemy import Column, Integer, String, ForeignKey, Table
from config.db_config import Base
from sqlalchemy.orm import relationship


class Expansion(Base):
    __tablename__ = "expansion"
    id = Column(Integer, primary_key=True, index=True)
    id_bgg = Column(Integer)
    value = Column(String(255))
    