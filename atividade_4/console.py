from marketplace import Marketplace
from textwrap import dedent


class Main:
    
    
    def menu():
        print(dedent('''\n 
                        -- Menu --
                        1. Lista Marketplaces
                        2. Lista Marketplace - Categorias
                        3. Lista Subcategorias - Categoria
                        4. Sair '''))
        op = int(input('Selecione a operação desejada: '))    
        return op
        
    while True:
        try:
            op = menu()

            m = Marketplace()

            if op == 1:
                m.listar_marketplaces()
            elif op == 2:
                m.listar_marketplace_categoria()
            elif op == 3:
                m.listar_categoria_subcategorias()
            elif op == 4:
                exit(0)    
            else:
                print('Opção invalida, tente novamente!')   
        except ValueError:
            print('Opção invalido, tente novamente!')        