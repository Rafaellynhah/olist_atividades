import sys
sys.path.append('.')

from src.models.category import Category


def test_name_none():
    try:
        c = Category(None, 'Bebida')
    except Exception as e:
        assert isinstance(e, TypeError)    
        
def test_name_empty():
    try:
        c = Category('', 'Bebida')
    except Exception as e:
        assert isinstance(e, ValueError)  
       
def test_name_len():
    try:
        c = Category('Bebida' * 100, 'Importada')
    except Exception as e:
        assert isinstance(e, ValueError)       
        
def test_name_type():
    try:
        c = Category(100, 'Importada')
    except Exception as e:
        assert isinstance(e, TypeError)                         
        
def test_description_type():
    try:
        c = Category('Bebida', 10.6)
    except Exception as e:
        assert isinstance(e, TypeError)           
        
def test_description_len():
    try:
        c = Category('Bebida', 'Importada' * 255)
    except Exception as e:
        assert isinstance(e, ValueError)          
