import sys
sys.path.append('.')

from back.model.product_model import Product
from back.model.base_model import BaseModel
import pytest


class TestProductModel:
    name = "Heineken"
    price = 5.99
    description = "Melhor cerveja"
    

    def test_istance(self):
        product = Product(self.name, self.price, self.description)
        assert isinstance(product, Product)
        assert isinstance(product, BaseModel)
        
        
    def test_empty_name(self):
        with pytest.raises(ValueError):
            product = Product("", self.price, self.description)


    def test_name_length(self):
        with pytest.raises(ValueError):
            product = Product("*" * 101, self.price, self.description)


    def test_name_type(self):
        with pytest.raises(TypeError):
            product = Product(101, self.price, self.description)    
            
            
    def test_price_zero(self):
        with pytest.raises(ValueError):
            product = Product(self.name, 0.0, self.description)


    def test_price_not_float(self):
        with pytest.raises(TypeError):
            product = Product(self.name, '', self.description)       
            
            
    def test_description_length(self):
        with pytest.raises(ValueError):
            product = Product(self.name, self.price, '*' * 201)


    def test_description_type(self):
        with pytest.raises(TypeError):
            product = Product(self.name, self.price ,201)      
         