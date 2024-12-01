from fastapi import APIRouter, HTTPException, Depends
from models.user import User, UserCreate
from services.db_service import (
    get_user_by_id, create_user, update_user, delete_user, get_all_users
)
from typing import List

router = APIRouter()

# Получение списка всех пользователей
@router.get("/", response_model=List[User], tags=["Users"])
def list_users():
    users = get_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="Пользователи не найдены")
    return users

# Получение пользователя по ID
@router.get("/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Пользователь с ID {user_id} не найден")
    return user

# Создание нового пользователя
@router.post("/", response_model=User, tags=["Users"])
def create_new_user(user: UserCreate):
    new_user = create_user(user)
    return new_user

# Обновление пользователя
@router.put("/{user_id}", response_model=User, tags=["Users"])
def update_existing_user(user_id: int, user: UserCreate):
    updated_user = update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail=f"Пользователь с ID {user_id} не найден")
    return updated_user

# Удаление пользователя
@router.delete("/{user_id}", tags=["Users"])
def delete_existing_user(user_id: int):
    success = delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Пользователь с ID {user_id} не найден")
    return {"message": "Пользователь удален"}
