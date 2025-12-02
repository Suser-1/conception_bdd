from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey


class UserGame(Base):
    __tablename__="user_game"
    
    id_game: Mapped[int] = mapped_column(Integer, ForeignKey("games.id_game"), primary_key=True)
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey("users.id_user"), primary_key=True)