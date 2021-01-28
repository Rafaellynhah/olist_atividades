from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        
    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name is not string') 
        if not name.strip():
            raise ValueError('Name can not be empty')
        if len(name) > 100:
            raise ValueError('Name can not more thank 100 characters')
        return name   
    
    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description is not string') 
        if len(description) > 255:
            raise ValueError('Description can not more thank 255 characters')
        return description   