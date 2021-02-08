from sqlalchemy import Column, String, Float
from back.model.base_model import BaseModel
from sqlalchemy.orm import validates
from back.utils.validators import *


class Product(BaseModel):
    __tablename__ = 'product04'
    name = Column('name', String(length=100), nullable=False)
    price = Column('price', Float(), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    

    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description
        

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_len(name, 100, key)
    
    
    @validates('price')
    def validate_price(self, key, price):
        price = validate_type(price, float, key)
        return validate_greater_than_zero(price, key)


    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        return validate_len(description, 100, key)
