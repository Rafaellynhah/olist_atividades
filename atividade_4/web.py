from flask import Flask, render_template, request
from marketplace import Marketplace


class Main:
    
    
    app = Flask(__name__)
    
    @app.route('/cadastro')
    def cadastrar_mkt():
        m = Marketplace()
        m.salvar_log('cadastrar_mkt')
        nome = request.args.get('nome_mkt')
        if nome != None:
            m.salvar_mkt_arq(nome)
        return render_template('cadastro.html')
            
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/marketplaces')
    def list_marketplaces():
        m = Marketplace()
        m.salvar_log('list_marketplaces')
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('marketplaces.html', list=lista)   
    
    @app.route('/categorias')
    def list_marketplaces_categorias():
        m = Marketplace()
        m.salvar_log('list_marketplaces_categorias')
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('categorias.html', list=lista)      
    
    @app.route('/subcategorias')
    def list_categoria_subcategorias():
        m = Marketplace()
        m.salvar_log('list_categoria_subcategorias')
        #lista = m.list_marketplaces()
        lista = m.ler_arquivo()
        return render_template('subcategorias.html', list=lista)    
         
    app.run(debug=True)    