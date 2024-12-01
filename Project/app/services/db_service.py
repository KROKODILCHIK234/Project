from database import SessionLocal
from models.user import User, UserCreate
from models.product import Product, ProductCreate
from models.order import Order, OrderCreate
from datetime import datetime

# Работа с пользователями
def get_user_by_id(user_id: int):
    with SessionLocal() as db:
        return db.query(User).filter(User.id == user_id).first()

def create_user(user: UserCreate):
    with SessionLocal() as db:
        db_user = User(name=user.name, email=user.email, is_active=True)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def update_user(user_id: int, user: UserCreate):
    with SessionLocal() as db:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            db.commit()
            db.refresh(db_user)
        return db_user

def delete_user(user_id: int):
    with SessionLocal() as db:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False

def get_all_users():
    with SessionLocal() as db:
        return db.query(User).all()

# Работа с продуктами
def get_product_by_id(product_id: int):
    with SessionLocal() as db:
        return db.query(Product).filter(Product.id == product_id).first()

def create_product(product: ProductCreate):
    with SessionLocal() as db:
        db_product = Product(
            name=product.name,
            price=product.price,
            description=product.description
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

def update_product(product_id: int, product: ProductCreate):
    with SessionLocal() as db:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            db_product.name = product.name
            db_product.price = product.price
            db_product.description = product.description
            db.commit()
            db.refresh(db_product)
        return db_product

def delete_product(product_id: int):
    with SessionLocal() as db:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            db.delete(db_product)
            db.commit()
            return True
        return False

def get_all_products():
    with SessionLocal() as db:
        return db.query(Product).all()

# Работа с заказами
def get_order_by_id(order_id: int):
    with SessionLocal() as db:
        return db.query(Order).filter(Order.id == order_id).first()

def create_order(order: OrderCreate):
    with SessionLocal() as db:
        db_order = Order(
            user_id=order.user_id,
            product_id=order.product_id,
            quantity=order.quantity,
            total_price=order.total_price,
            order_date=datetime.now()
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

def update_order(order_id: int, order: OrderCreate):
    with SessionLocal() as db:
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if db_order:
            db_order.user_id = order.user_id
            db_order.product_id = order.product_id
            db_order.quantity = order.quantity
            db_order.total_price = order.total_price
            db.commit()
            db.refresh(db_order)
        return db_order

def delete_order(order_id: int):
    with SessionLocal() as db:
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if db_order:
            db.delete(db_order)
            db.commit()
            return True
        return False

def get_all_orders():
    with SessionLocal() as db:
        return db.query(Order).all()
