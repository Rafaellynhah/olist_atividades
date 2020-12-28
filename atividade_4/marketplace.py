class Marketplace:
    
    
    # def list_marketplaces(self):
    #     marketplaces = [{'Marketplace': 'Americanas', 'Categoria': 'Eletronicos', 'Subcategoria': ['Celulares', 'Tvs']},
    #                                {'Marketplace': 'Submarino', 'Categoria': 'Moveis', 'Subcategoria': ['Sofá', 'Cama']},
    #                                {'Marketplace': 'Casas Bahia', 'Categoria': 'Limpeza', 'Subcategoria': ['Piso', 'Vidro']}]
    #     return marketplaces
    
    # def listar_marketplaces(self):
    #     mkt = self.list_marketplaces()
    #     for i in range(len(mkt)):
    #         print(f'[{i}]. ' + mkt[i]['Marketplace'])
            
    # def listar_marketplace_categoria(self):
    #     mkt = self.list_marketplaces()
    #     for i in range(len(mkt)):
    #         print(f'[{i}]. ' + 'Marketplace: {}, Categoria: {}'.format(mkt[i]['Marketplace'], mkt[i]['Categoria']))  
            
    # def listar_categoria_subcategorias(self):
    #     mkt = self.list_marketplaces()
    #     for i in range(len(mkt)):
    #         print(f'[{i}]. ' + 'Categoria: {}, Subcategoria: {}'.format(mkt[i]['Categoria'], mkt[i]['Subcategoria']))  
    
    def ler_arquivo(self) -> list:
        list_arq = []
        arq = open('marketplace.txt', 'r')
        for l in arq:
            linha = l.strip()
            linha = linha.split(';') 
            list_arq.append(linha)
        arq.close()
        return list_arq                   
            
    def listar_marketplaces(self):
        mkt = self.ler_arquivo()
        for l in mkt:
            print(f'Marketplace: {l[0]}')
     
    def listar_marketplace_categoria(self):
        mkt = self.ler_arquivo()
        for l in mkt:
            print(f'Marketplace: {l[0]}, Categoria: {l[1]}')
                        
    def listar_categoria_subcategorias(self):
        mkt = self.ler_arquivo()
        for l in mkt:
            print(f'Categoria: {l[1]}, Subcategoria: {l[2]}')
                            