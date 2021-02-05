from sqlalchemy import Column, String, Float
from back.model.base_model import BaseModel
from sqlalchemy.orm import validates
from back.utils.validator import validate_greater_than_zero, validate_len, validate_not_empty, validate_type

class Product(BaseModel):
    __tablename__ = 'product04'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    price = Column('price', Float(), nullable=False)

    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.description = description
        self.price = price

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        name = validate_len(name, 100, key)
        return name

    @validates('description')
    def validate_description(self, key, description):
        if description is None:
            return description
        description = validate_type(description, str, key)
        return validate_len(description, 255, key)

    @validates('price')
    def validate_price(self, key, price):
        price = validate_type(price, float, key)
        return validate_greater_than_zero(price, key)
