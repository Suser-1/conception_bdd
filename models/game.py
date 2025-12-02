from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from models.user_game import UserGame
from models.game_publisher import GamePublisher
from models.game_platform import GamePlatform
from models.game_genre import GameGenre

from models.user import User
from models.sale import Sale
from models.publisher import Publisher
from models.platform import Platform
from models.genre import Genre


class Game(Base):
    __tablename__= "games" 
    
    id_game: Mapped[int] = mapped_column(Integer, primary_key=True)
    rank_game: Mapped[int] = mapped_column(Integer, nullable=False)
    name_game: Mapped[str]= mapped_column(String(100), nullable=False)
    
    users= relationship("User", secondary="user_game", back_populates="games")
    publishers = relationship("Publisher", secondary="game_publisher", back_populates="games")
    genres = relationship("Genre", secondary="game_genre", back_populates="games")
    platforms = relationship("Platform", secondary="game_platform", back_populates="games")
    sales= relationship("Sale", back_populates="game")