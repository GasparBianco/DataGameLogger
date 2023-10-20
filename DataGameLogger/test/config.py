from models.boardgame import UserBoardGameCollection
from models.user import User
from models.friends import Friends
from models.db_config import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from fastapi.testclient import TestClient

database_name = "DataGameLogger_Test"
user = "postgres"
password = "postgres"
db_url = f"postgresql+psycopg2://{user}:{password}@localhost/{database_name}"

engine = create_engine(db_url)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


Base.metadata.create_all(bind=engine)