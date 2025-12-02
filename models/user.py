from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, Boolean
from datetime import date
from models.user_game import UserGame


class User(Base):
    __tablename__= "users"
    
    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    pseudo_user: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    mail_user: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    consent_user: Mapped[bool] = mapped_column(Boolean)
    limitdate_user: Mapped[date] = mapped_column(Date, nullable=False)
    password_user:Mapped[str] =mapped_column(String(200), nullable=False)
    
    games = relationship("Game", secondary="user_game", back_populates="users")