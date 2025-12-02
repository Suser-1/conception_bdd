from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from models.game_genre import GameGenre


class Genre(Base):
    __tablename__="genres"
    
    id_genre: Mapped[int] = mapped_column(Integer, primary_key=True)
    type_genre: Mapped[str] = mapped_column(String(20))
    
    games = relationship("Game", secondary="game_genre", back_populates="genres")