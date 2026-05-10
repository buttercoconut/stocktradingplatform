# backend/app/services/order_service.py
from sqlalchemy.orm import Session
from ..models.order import Order, OrderStatus
from ..models.stock import Stock
from ..models.user import User

class OrderService:
    def __init__(self, db: Session):
        self.db = db

    def place_order(self, user_id: int, stock_symbol: str, quantity: int, side: str):
        # Retrieve stock price from DB (in real scenario, fetch from market data)
        stock = self.db.query(Stock).filter(Stock.symbol == stock_symbol).first()
        if not stock:
            raise ValueError("Stock not found")
        # Calculate price (simplified: use current market price)
        price = stock.price
        order = Order(user_id=user_id, stock_id=stock.id, quantity=quantity, price=price, side=side, status=OrderStatus.PENDING)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        # Simulate execution
        order.status = OrderStatus.EXECUTED
        self.db.commit()
        self.db.refresh(order)
        return order
