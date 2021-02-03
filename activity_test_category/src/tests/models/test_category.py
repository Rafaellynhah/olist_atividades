import sys
sys.path.append('.')

from src.models.category import Category
import pytest

        
def test_name_empty():
    with pytest.raises(ValueError):
        categories = Category("", "Description")  

       
def test_name_len():
    with pytest.raises(ValueError):
        categories = Category("Large name example." * 100, "Description")

        
def test_name_type():
    with pytest.raises(TypeError):
        categories = Category(100, "Description")      

        
def test_description_type():
    with pytest.raises(TypeError):
        categories = Category("Name", 10)     

        
def test_description_len():
    with pytest.raises(ValueError):
        categories = Category("Large name example.", "Description" * 500)          
