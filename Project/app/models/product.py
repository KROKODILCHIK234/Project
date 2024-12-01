from pydantic import BaseModel

# Основная модель для продукта
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

    class Config:
        orm_mode = True

# Модель для создания нового продукта
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
