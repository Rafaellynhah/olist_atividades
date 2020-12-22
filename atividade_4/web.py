from flask import Flask, render_template


class Main:
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/marketplaces')
    def list_marketplaces():
        marketplaces = ['Americanas', 'Submarino', 'Casas Bahia', 'PontoFrio']
        return render_template('markeplaces.html', list=marketplaces)   
    
    @app.route('/categorias')
    def list_marketplaces_categorias():
        marketplaces_categorias = [['Americanas', ['Eletronico', ['Celulares', 'Tvs']]]]
        return render_template('categorias.html', list=marketplaces_categorias)      
         
    app.run()    