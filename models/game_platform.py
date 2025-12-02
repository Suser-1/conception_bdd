from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey


class GamePlatform(Base):
    __tablename__="game_platform"
    
    id_game: Mapped[int] = mapped_column(Integer, ForeignKey("games.id_game"), primary_key=True)
    id_platform: Mapped[int] = mapped_column(Integer, ForeignKey("platforms.id_platform"), primary_key=True)
    release_year: Mapped[int] = mapped_column(Integer, nullable=True)