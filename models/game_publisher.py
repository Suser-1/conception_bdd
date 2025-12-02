from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey


class GamePublisher(Base):
    __tablename__="game_publisher"
    
    id_game: Mapped[int] = mapped_column(Integer, ForeignKey("games.id_game"), primary_key=True)
    id_publisher: Mapped[int] = mapped_column(Integer, ForeignKey("publishers.id_publisher"), primary_key=True)