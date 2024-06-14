import datetime
from typing import Optional

from pydantic import EmailStr
from sqlalchemy import String, ForeignKey, DateTime, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

'''Переменная metadata действительно не нужна в вашем коде, так как вы используете декларативный стиль 
определения моделей с помощью SQLAlchemy ORM, который сам управляет метаданными. Убедитесь, 
что вы вызываете Base.metadata.create_all(engine) вместо metadata.create_all(engine) для создания таблиц.'''


class Base(DeclarativeBase):
    ...


class Role(Base):
    __tablename__ = 'Role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class User(Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(30))
    degree: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    email: Mapped[EmailStr] = mapped_column(String(50), unique=True, nullable=False)
    registered_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.date)
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    is_active: Mapped[bool] = mapped_column(String(100))
    is_superuser: Mapped[bool] = mapped_column(String(100))
    is_verified: Mapped[bool] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, role={self.role!r})"


class Trade(Base):
    __tablename__ = 'Trade'

    trade_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    currency: Mapped[str] = mapped_column(String(15))
    side: Mapped[str] = mapped_column(String(15))
    price: Mapped[float] = mapped_column(Float)
    amount: Mapped[float] = mapped_column(Float)

    def __repr__(self) -> str:
        return (f"Trade(trade_id={self.trade_id!r}, user_id={self.user_id!r}, currency={self.currency!r}, "
                f"side={self.side!r}, price={self.price!r}, amount={self.amount!r})")


# Создание таблиц в базе данных.
metadata = Base.metadata
