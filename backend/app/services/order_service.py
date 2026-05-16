from typing import Dict
from uuid import uuid4
from datetime import datetime
from ..models.order import Order

# In-memory store for demo purposes
orders_db: Dict[int, Order] = {}

async def process_order(order_data) -> Order:
    """Core order processing logic.
    1. Validate order
    2. Interact with brokerage API (mocked)
    3. Persist order
    4. Publish event to Kafka (mocked)
    """
    # 1. Validation
    if order_data.side not in ("buy", "sell"):
        raise ValueError("Invalid side")
    if order_data.quantity <= 0:
        raise ValueError("Quantity must be positive")

    # 2. Mock brokerage API call
    # In real implementation, call external REST API and handle response
    brokerage_response = {
        "status": "filled",
        "executed_price": order_data.quantity * 100.0,  # dummy price
        "timestamp": datetime.utcnow().isoformat(),
    }

    # 3. Persist order
    order_id = len(orders_db) + 1
    new_order = Order(
        order_id=order_id,
        user_id=order_data.user_id,
        symbol=order_data.symbol,
        quantity=order_data.quantity,
        side=order_data.side,
        status=brokerage_response["status"],
        price=brokerage_response["executed_price"],
    )
    orders_db[order_id] = new_order

    # 4. Publish event (mock)
    # In real code, produce to Kafka topic
    # e.g., await kafka_producer.send("orders", value=order_id)

    return new_order
