from pydantic import BaseModel, EmailStr

# Основная модель для пользователя
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

# Модель для создания нового пользователя
class UserCreate(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
