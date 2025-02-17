
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Computed
from typing import List
from datetime import date


class Model(DeclarativeBase):
    pass



class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    surname : Mapped[str]
    email : Mapped[str]
    password : Mapped[str]




class Product(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    description : Mapped[str]
    price : Mapped[float]
    quantity : Mapped[int] = mapped_column(default=0)
    img_path : Mapped[str]
    views : Mapped[List["View"]] = relationship("View", back_populates="product")



class View(Model):
    __tablename__ = "views"

    id: Mapped[int] = mapped_column(primary_key=True)
    at : Mapped[date] = mapped_column(default=date.today)
    view : Mapped[int] = mapped_column(default=0)
    product_id : Mapped[int] = mapped_column(ForeignKey("products.id"))
    product : Mapped["Product"] = relationship("Product", back_populates="views", lazy="selectin")








