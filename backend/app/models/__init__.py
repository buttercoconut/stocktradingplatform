from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime

class Stock(BaseModel):
    symbol: str
    name: str
    price: float
    last_updated: datetime

class Order(BaseModel):
    id: int
    user_id: int
    symbol: str
    quantity: int
    price: float
    side: str  # "buy" or "sell"
    status: str
    created_at: datetime
