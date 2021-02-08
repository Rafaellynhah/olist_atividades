from src.dao.session import Session
from src.models.base_model import BaseModel


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model


    def save(self, obj: BaseModel) -> None:
        with Session() as s:
            s.add(obj)
            s.commit()
            s.refresh(obj)
            return obj


    def read_all(self) -> list:
        with Session() as s:
            result = s.query(self.__type_model).all()   
        return result


    def read_by_id(self, id:int) -> BaseModel:
        if isinstance(id, int):
            with Session() as s:
                result = s.query(self.__type_model).filter_by(id=id).first()
            return result 
        else:
            raise TypeError('ID must be integer.')


    def delete(self, obj: BaseModel) -> None:
        with Session() as s:
            s.delete(obj)
            s.commit()  