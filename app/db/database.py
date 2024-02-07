from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from core.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Function to check the database connection
def check_db_connection():
    try:
        # Create a session to check the connection
        with engine.connect() as db:
            db.execute(text("SELECT 1"))
            return True
    except OperationalError as e:
        return False


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
