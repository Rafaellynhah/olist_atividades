import pytest
import sys
sys.path.append('.')

from src.models.category_model import Category
from src.dao.category_dao import CategoryDao

class TestCategoryDao:
    @pytest.fixture
    def create_instance(self) -> Category:
        category = Category("Name", "Description")
        return category

    def test_instance(self):
        dao = CategoryDao()
        assert isinstance(dao, CategoryDao)

    def test_save_new_category(self, create_instance):
        dao = CategoryDao()
        category = create_instance
        new_category = dao.save(category)

        assert new_category.id is not None
        assert new_category.name == category.name
        assert new_category.description == category.description
        dao.delete(new_category)

    def test_save_existing_category(self, create_instance):
        dao = CategoryDao()
        category = create_instance
        new_category = dao.save(category)
        category.name = 'NewCategory'
        category.description = 'NewDescription'

        updated_category = dao.save(new_category)
        assert updated_category.description is category.description
        assert updated_category.name is category.name
        dao.delete(updated_category)
    
    def test_delete_category(self, create_instance):
        dao = CategoryDao()
        new_category = dao.save(create_instance)
        dao.delete(new_category)
        deleted_category = dao.read_by_id(new_category.id)

        assert deleted_category is None
    
    def test_read_by_id(self, create_instance):
        dao = CategoryDao()
        category = create_instance
        new_category = dao.save(category)

        assert isinstance(new_category, Category)
        assert category.id is not None
        assert new_category.name == category.name
        assert new_category.description == category.description
        dao.delete(new_category)

    def test_read_all(self):
        categories = CategoryDao().read_all()

        assert isinstance(categories, list)