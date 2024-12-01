from pydantic import BaseModel
from datetime import datetime

# Основная модель для заказа
class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: float
    order_date: datetime

    class Config:
        orm_mode = True

# Модель для создания нового заказа
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float
