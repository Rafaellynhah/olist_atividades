from flask import Flask, render_template
from marketplace import Marketplace
import logging


class Main:
    
    logging.TRACE = 10
    logging.basicConfig(filename='log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(funcName)s')
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/marketplaces')
    def list_marketplaces():
        logging.debug('')
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('marketplaces.html', list=lista)   
    
    @app.route('/categorias')
    def list_marketplaces_categorias():
        logging.debug('')
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('categorias.html', list=lista)      
    
    @app.route('/subcategorias')
    def list_categoria_subcategorias():
        logging.debug('')
        m = Marketplace()
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('subcategorias.html', list=lista)    
         
    app.run(debug=True)    