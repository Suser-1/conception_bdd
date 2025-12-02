from database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, Float, ForeignKey


class Sale(Base):
    __tablename__= "sales"
    
    id_sale: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    na_sales: Mapped[float] = mapped_column(Float, nullable=False)
    eu_sales: Mapped[float] = mapped_column(Float, nullable=False)
    jp_sales: Mapped[float] =mapped_column(Float, nullable=False)
    other_sales: Mapped[float] =  mapped_column(Float, nullable=False)
    global_sales: Mapped[float] =  mapped_column(Float, nullable=False)
    id_game: Mapped[int] = mapped_column(Integer, ForeignKey("games.id_game"))
    
    game = relationship("Game", back_populates="sales")