# backend/app/api/stock.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.stock_service import StockService

router = APIRouter(prefix="/stocks", tags=["stocks"])

@router.get("/{symbol}")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    service = StockService(db)
    stock = service.get_stock(symbol)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.get("/")
def list_stocks(db: Session = Depends(get_db)):
    service = StockService(db)
    return service.list_stocks()
