from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from models.game_platform import GamePlatform


class Platform(Base):
    __tablename__="platforms"
    
    id_platform: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_platform: Mapped[str] = mapped_column(String(100), nullable=False)
    
    games = relationship("Game", secondary="game_platform", back_populates="platforms")