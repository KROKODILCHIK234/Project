import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from app.database import Base  # Базовый класс моделей SQLAlchemy
from app.models import user_model, product_model, order_model  # Все модели

# Добавляем путь к вашему проекту в sys.path, чтобы импортировать модули
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

# Настройки Alembic
config = context.config

# Настройка логгирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем метаданные моделей для Alembic
target_metadata = Base.metadata

# Функция для подключения к базе данных и выполнения миграций
def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Функция для подключения к базе данных и выполнения миграций в онлайн режиме
def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Выбор между онлайн и оффлайн режимами
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
