import sqlmodel 
import time
from sqlmodel import SQLModel, Session
from .config import DB_URL

if DB_URL == "":
    raise NotImplementedError("DB_URL is not set")

engine = sqlmodel.create_engine(DB_URL)

def init_db():
    print("creating db")
    max_retries = 30
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            SQLModel.metadata.create_all(engine)
            print("Database initialized successfully")
            return
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Database connection failed (attempt {attempt + 1}/{max_retries}): {e}")
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Failed to initialize database after {max_retries} attempts")
                raise

def get_session():
    with Session(engine) as session:
        yield session