import sys
sys.path.append('.')

from src.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao) -> None:
        self.__dao = dao


    def save(self, obj: BaseModel) -> None:
        self.__dao.save(obj)


    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        if result:
            return result
        raise Exception('Object not found in the database.')


    def read_all(self) -> list:
        lista = self.__dao.read_all()
        return lista


    def delete(self, obj: BaseModel) -> None:
        self.__dao.delete(obj)