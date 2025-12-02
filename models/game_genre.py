from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey


class GameGenre(Base):
    __tablename__="game_genre"
    
    id_game: Mapped[int] = mapped_column(Integer, ForeignKey("games.id_game"), primary_key=True)
    id_genre: Mapped[int] = mapped_column(Integer, ForeignKey("genres.id_genre"), primary_key=True)