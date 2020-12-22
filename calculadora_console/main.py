from calculadora import Calculadora

class Main:
    
    def menu():
        operacao = int(input(''' 
    -- Calculadora --
    1. Adição
    2. Subtração
    3. Divisão
    4. Multiplicação
    5. Sair
    Selecione a operação desejada: '''))    
        return operacao
        
    while True:
        try:
            operacao = menu()
            
            n1 = float(input('Digite o primeiro numero: '))
            n2 = float(input('Digite o segundo numero: '))
            
            c = Calculadora()
            resultado = None
            if operacao == 1:
                resultado = c.adicao(n1,n2)
            elif operacao == 2:
                resultado = c.subtracao(n1,n2)
            elif operacao == 3:
                resultado = c.divisao(n1,n2)     
            elif operacao == 4:
                resultado = c.multiplicacao(n1,n2)
            elif operacao == 5:
                exit(0)    
            else:
                print('Operação invalida, tente novamente!') 
            if resultado:
                print(f'\nResultado: {resultado}')     
        except ValueError:
            print('Valor invalido, tente novamente!')        