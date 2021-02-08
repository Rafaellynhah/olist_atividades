import pytest
import sys
sys.path.append('.')

from src.models.category_model import Category
from src.controller.category_controller import CategoryController


class TestCategoryController:
    @pytest.fixture
    def create_instance_model(self):
        category = Category('Name', 'Description')
        return category
    
    @pytest.fixture
    def create_instance_controller(self):
        controller = CategoryController()
        return controller
    
    def test_save_new_category(self, create_instance_model, create_instance_controller):
        controller = create_instance_controller
        category = create_instance_model
        new_category = controller.save(create_instance_model)

        assert new_category.id is not None
        assert new_category.name == category.name
        assert new_category.description == category.description

        controller.delete(category)
    
    def test_save_existing_category(self, create_instance_model, create_instance_controller):
        controller = create_instance_controller
        category = create_instance_model
        
        controller.save(create_instance_model)
        
        category.name = 'NewName'
        category.description = 'NewDescription'
        updated_category = controller.save(category)

        assert updated_category.id is not None
        assert updated_category.name == category.name
        assert updated_category.description == category.description

        controller.delete(category)

    def test_read_all(self, create_instance_controller):
        controller = create_instance_controller
        categories = controller.read_all()

        assert isinstance(categories, list)

    def test_read_by_id(self, create_instance_model, create_instance_controller):
        controller = create_instance_controller
        category = create_instance_model
        new_category = controller.save(category)

        assert isinstance(new_category, Category)
        assert new_category.id == category.id
        assert new_category.name == category.name
        assert new_category.description == category.description
        controller.delete(new_category)
