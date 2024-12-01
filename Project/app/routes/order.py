from fastapi import APIRouter, HTTPException
from models.order import Order, OrderCreate
from services.db_service import (
    get_order_by_id, create_order, update_order, delete_order, get_all_orders
)
from typing import List

router = APIRouter()

# Получение всех заказов
@router.get("/", response_model=List[Order], tags=["Orders"])
def list_orders():
    orders = get_all_orders()
    if not orders:
        raise HTTPException(status_code=404, detail="Заказы не найдены")
    return orders

# Получение заказа по ID
@router.get("/{order_id}", response_model=Order, tags=["Orders"])
def get_order(order_id: int):
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказ с ID {order_id} не найден")
    return order

# Создание нового заказа
@router.post("/", response_model=Order, tags=["Orders"])
def create_new_order(order: OrderCreate):
    new_order = create_order(order)
    return new_order

# Обновление заказа
@router.put("/{order_id}", response_model=Order, tags=["Orders"])
def update_existing_order(order_id: int, order: OrderCreate):
    updated_order = update_order(order_id, order)
    if not updated_order:
        raise HTTPException(status_code=404, detail=f"Заказ с ID {order_id} не найден")
    return updated_order

# Удаление заказа
@router.delete("/{order_id}", tags=["Orders"])
def delete_existing_order(order_id: int):
    success = delete_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Заказ с ID {order_id} не найден")
    return {"message": "Заказ удален"}
