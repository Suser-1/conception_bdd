from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from models.game_publisher import GamePublisher


class Publisher(Base):
    __tablename__= "publishers"
    
    id_publisher:Mapped[int] = mapped_column(Integer, primary_key=True)
    name_publisher:Mapped [str] = mapped_column(String(100), unique=True, nullable=False)
    
    games = relationship("Game", secondary="game_publisher", back_populates="publishers")