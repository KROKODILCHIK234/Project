from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes import user, product, order
from database import engine, Base
import logging
from logging.handlers import RotatingFileHandler
#from app import app

# Настройка логирования
log_handler = RotatingFileHandler("logs/app.log", maxBytes=2000, backupCount=5)
logging.basicConfig(handlers=[log_handler], level=logging.INFO)

# Создание экземпляра приложения
app = FastAPI(
    title="ISZF API",
    description="""
    API для управления пользователями, продуктами и заказами. 
    Включает расширенную поддержку маршрутов, методов и обработчиков ошибок.
    """,
    version="2.0.0",
    docs_url="/docs",  # Путь для Swagger документации
    redoc_url="/redoc",  # Путь для Redoc
)

# CORS настройки
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])

# Событие старта приложения
@app.on_event("startup")
def startup():
    logging.info("Приложение запущено, создаем таблицы...")
    Base.metadata.create_all(bind=engine)
    logging.info("Таблицы созданы успешно.")

# Главная страница
@app.get("/", tags=["Root"])
def root():
    logging.info("Запрос на главную страницу.")
    return {"message": "Добро пожаловать в ISZF API", "documentation": "/docs"}

# Маршрут для проверки статуса сервера
@app.get("/status", tags=["Status"])
def status():
    logging.info("Проверка статуса сервера.")
    return {"status": "Сервер работает", "uptime": "3 days", "version": "2.0.0"}

# Обработка ошибок
@app.exception_handler(HTTPException)
def handle_exception(request, exc):
    logging.error(f"Ошибка: {exc.detail}")
    return {"error": exc.detail, "code": exc.status_code}

# Пример сложного обработчика запроса
@app.post("/validate/", tags=["Validation"])
def validate_data(data: dict):
    logging.info(f"Полученные данные для проверки: {data}")
    if not data.get("field"):
        raise HTTPException(status_code=400, detail="Поле 'field' отсутствует")
    return {"valid": True, "data": data}
