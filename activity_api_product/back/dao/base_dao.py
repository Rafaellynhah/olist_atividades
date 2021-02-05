from back.dao.session import Session
from back.model.base_model import BaseModel

class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model
    
    def save(self, model: BaseModel) -> None:
        with Session() as s:
            s.add(model)
            s.commit()
            s.refresh(model)
            return model


    def read_all(self) -> list:
        with Session() as s:
            result = s.query(self.__type_model).order_by('id').all()
        return result


    def read_by_id(self, id:int) -> BaseModel:
        if isinstance(id, int):
            with Session() as s:
                result = s.query(self.__type_model).filter_by(id=id).first()
            return result
        else:
            raise TypeError('Id must be integer')

    def delete(self, model: BaseModel) -> None:
        with Session() as s:
            s.delete(model)
            s.commit()
            
