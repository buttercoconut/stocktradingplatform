from pydantic import BaseModel

class Order(BaseModel):
    order_id: int
    user_id: int
    symbol: str
    quantity: int
    side: str
    status: str
    price: float
