# backend/app/models/stock.py
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    exchange = Column(String, nullable=False)
