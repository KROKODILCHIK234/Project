from fastapi import APIRouter, HTTPException
from models.product import Product, ProductCreate
from services.db_service import (
    get_product_by_id, create_product, update_product, delete_product, get_all_products
)
from typing import List

router = APIRouter()

# Получение всех продуктов
@router.get("/", response_model=List[Product], tags=["Products"])
def list_products():
    products = get_all_products()
    if not products:
        raise HTTPException(status_code=404, detail="Продукты не найдены")
    return products

# Получение продукта по ID
@router.get("/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Продукт с ID {product_id} не найден")
    return product

# Создание нового продукта
@router.post("/", response_model=Product, tags=["Products"])
def create_new_product(product: ProductCreate):
    new_product = create_product(product)
    return new_product

# Обновление продукта
@router.put("/{product_id}", response_model=Product, tags=["Products"])
def update_existing_product(product_id: int, product: ProductCreate):
    updated_product = update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail=f"Продукт с ID {product_id} не найден")
    return updated_product

# Удаление продукта
@router.delete("/{product_id}", tags=["Products"])
def delete_existing_product(product_id: int):
    success = delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Продукт с ID {product_id} не найден")
    return {"message": "Продукт удален"}
