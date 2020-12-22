from calculadora import Calculadora
from flask import Flask, render_template


class Main:
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/adicao')
    def adicao():
        c = Calculadora()
        n1 = 2.0
        n2 = 23.0
        resultado = c.adicao(n1, n2)
        return render_template('adicao.html', n1=n1, n2=n2, r=resultado)
    
    @app.route('/subtracao')    
    def subtracao():
        c = Calculadora()
        n1 = 34.0
        n2 = 25.0
        resultado = c.subtracao(n1, n2)
        return render_template('subtracao.html', n1=n1, n2=n2, r=resultado)
    
    @app.route('/multiplicacao')
    def multiplicacao():
        c = Calculadora()
        n1 = 3.0
        n2 = 12.0
        resultado = c.multiplicacao(n1, n2)
        return render_template('multiplicacao.html', n1=n1, n2=n2, r=resultado)
    
    @app.route('/divisao')
    def divisao():
        c = Calculadora()
        n1 = 34.0
        n2 = 2.0
        resultado = c.divisao(n1, n2)
        return render_template('divisao.html', n1=n1, n2=n2, r=resultado)                
         
    app.run()    