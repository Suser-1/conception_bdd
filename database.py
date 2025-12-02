from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///library_games.db"

engine = create_engine("sqlite:///library_games.db")
class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine
)