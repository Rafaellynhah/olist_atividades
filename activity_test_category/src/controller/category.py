import sys
sys.path.append('.')

from src.dao.category import CategoryDao
from src.models.category import Category


class CategoryController:
    def __init__(self) -> None:
        self.__dao = CategoryDao()

    def save(self, model: Category) -> Category:
        new_category = self.__dao.save(model)
        return new_category

    def delete(self, model: Category) -> None:
        self.__dao.delete(model)

    def read_all(self) -> list[Category]:
        categories = self.__dao.read_all()
        return categories
    
    def read_by_id(self, identifier) -> Category:
        category = self.__dao.read_by_id(identifier)
        return category
