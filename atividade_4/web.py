from flask import Flask, render_template
from marketplace import Marketplace


class Main:
    
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/marketplaces')
    def list_marketplaces():
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('marketplaces.html', list=lista)   
    
    @app.route('/categorias')
    def list_marketplaces_categorias():
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('categorias.html', list=lista)      
    
    @app.route('/subcategorias')
    def list_categoria_subcategorias():
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('subcategorias.html', list=lista)    
         
    app.run(debug=True)    