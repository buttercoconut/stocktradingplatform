# backend/app/services/stock_service.py
from sqlalchemy.orm import Session
from ..models.stock import Stock

class StockService:
    def __init__(self, db: Session):
        self.db = db

    def get_stock(self, symbol: str):
        return self.db.query(Stock).filter(Stock.symbol == symbol).first()

    def list_stocks(self):
        return self.db.query(Stock).all()
