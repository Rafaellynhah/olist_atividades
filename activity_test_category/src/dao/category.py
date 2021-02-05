import sys
sys.path.append('.')

from src.models.category import Category
from src.dao.session import Session


class CategoryDao:
    def save(self, model: Category) -> Category:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model
        
    def delete(self, model: Category) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()

    def read_all(self) -> list[Category]:
        with Session() as session:
            result = session.query(Category).order_by('id').all()
        return result

    def read_by_id(self, identifier: int) -> Category:
        with Session() as session:
            result = session.query(Category).filter_by(id = identifier).first()
        return result
