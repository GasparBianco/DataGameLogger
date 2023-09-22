from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


database_name = "DataGameLogger"
user = "postgres"
password = "postgres"

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost/{database_name}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
