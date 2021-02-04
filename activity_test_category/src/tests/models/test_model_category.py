import pytest
import sys
sys.path.append('.')

from src.models.category import Category

class TestCategoryModel:
    def create_instance(self):
        categories = Category("Name", "Description")

    def test_name_empty(self):
        with pytest.raises(ValueError):
            categories = Category("", "Description")

    def test_name_len(self):
        with pytest.raises(ValueError):
            categories = Category("Large name example." * 100, "Description")
            
    def test_name_type(self):
        with pytest.raises(TypeError):
            categories = Category(100, "Description")      
            
    def test_description_type(self):
        with pytest.raises(TypeError):
            categories = Category("Name", 10) 

    def test_description_len(self):
        with pytest.raises(ValueError):
            categories = Category("Large name example.", "Description" * 500)          
