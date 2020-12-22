class Calculadora:
    
    
    def adicao(self, n1:float, n2:float) -> float:
        if self.valida_float(n1) and self.valida_float(n2):
            resultado = n1 + n2
            return resultado
    
    def subtracao(self, n1:float, n2:float) -> float:
        if self.valida_float(n1) and self.valida_float(n2):
            resultado = n1 - n2
            return resultado

    def multiplicacao(self, n1:float, n2:float) -> float:
        if self.valida_float(n1) and self.valida_float(n2):
            resultado = n1 * n2
            return resultado

    def divisao(self, n1:float, n2:float) -> float:
        try:
            if self.valida_float(n1) and self.valida_float(n2):
                resultado = n1 / n2
                return resultado  
        except ZeroDivisionError as zero_e:
            raise zero_e        
        
    def valida_float(self, n:float)->bool:
        if isinstance(n, float):
            return True
        raise ValueError(f'O valor informado {n} não é um float!')    