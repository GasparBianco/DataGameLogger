from models.boardgame import UserBoardGameCollection
from models.user import User
from models.friends import Friends
from models.db_config import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from fastapi.testclient import TestClient
import pytest

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

@pytest.fixture(scope="session", autouse=True)
def clean_database():
    db = TestingSessionLocal()
    trans = db.begin()
    
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        db.close()

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200