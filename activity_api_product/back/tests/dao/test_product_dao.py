import sys
sys.path.append('.')

from sqlalchemy.orm.exc import UnmappedInstanceError
from back.dao.product_dao import ProductDao
from back.model.product_model import Product
import pytest


class TestProductDao:
    @pytest.fixture
    def create_instance(self):
        product = Product('Heineken', 5.99, 'Melhor cerveja')
        return product


    def test_instance(self):
        product_dao = ProductDao()
        assert isinstance(product_dao, ProductDao)


    def test_save(self, create_instance):
        product_saved = ProductDao().save(create_instance)
        assert product_saved.id is not None
        ProductDao().delete(product_saved)


    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            product_saved = ProductDao().save('product')


    def test_read_by_id(self, create_instance):
        product_saved = ProductDao().save(create_instance)
        product_read = ProductDao().read_by_id(product_saved.id)
        assert isinstance(product_read, Product)
        ProductDao().delete(product_read)


    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            product_read = ProductDao().read_by_id('id')


    def test_read_all(self):
        result = ProductDao().read_all()
        assert isinstance(result, list)


    def test_delete(self, create_instance):
        product_saved = ProductDao().save(create_instance)
        product_read = ProductDao().read_by_id(product_saved.id)
        ProductDao().delete(product_read)
        product_read = ProductDao().read_by_id(product_saved.id)

        assert product_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            ProductDao().delete('product.id')
