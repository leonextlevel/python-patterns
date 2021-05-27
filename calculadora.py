from abc import ABC, abstractmethod


class Operacao(ABC):

    @abstractmethod
    def calcular_operacao(self, a: int, b: int):
        pass


class Adicao(Operacao):

    precedencia = 1

    def calcular_operacao(self, a: int, b: int):
        return a + b


class Subtracao(Operacao):

    precedencia = 1

    def calcular_operacao(self, a: int, b: int):
        return a - b


class Multiplicacao(Operacao):

    precedencia = 2

    def calcular_operacao(self, a: int, b: int):
        return a * b


class Divisao(Operacao):

    precedencia = 2

    def calcular_operacao(self, a: int, b: int):
        return a / b


class TipoCalculadora(ABC):
    
    @abstractmethod
    def run(self, lista_expressao: list, operacoes: dict):
        pass


class CalculadoraPosfixa(TipoCalculadora):
    def run(self, lista_expressao: list, operacoes: dict):
        operandos = []
        for item in lista_expressao:
            if item.isnumeric():
                operandos.append(float(item))
            else:
                operando2 = operandos.pop()
                operando1 = operandos.pop()
                result = operacoes[item].calcular_operacao(operando1, operando2)
                operandos.append(result)
        return operandos.pop()


class CalculadoraInfixa(TipoCalculadora):
    # coverter para posfixa e calcular igual
    def run(self, lista_expressao: list, operacoes: dict):
        posfixa = []
        aux = []
        for item in lista_expressao:
            # trata quando é numero
            if item.isnumeric():
                posfixa.append(item)

            # trata quando é parenteses
            elif item == '(':
                aux.append(item)
            elif item == ')':
                while not aux and aux[-1] == '(':
                    posfixa.append(aux.pop())
                aux.pop()
            
            # Tratando operadores
            else:
                while aux and operacoes[aux[-1]].precedencia >= operacoes[item].precedencia:
                    posfixa.append(aux.pop())
                aux.append(item)
        # pega o que restou da lista auxiliar
        while aux:
            posfixa.append(aux.pop())

        return CalculadoraPosfixa().run(posfixa, operacoes)


class CalculadoraPrefixa(TipoCalculadora):
    def run(self, lista_expressao: list, operacoes: dict):
        posfixa = []
        lista_expressao = lista_expressao[::-1]
        for item in lista_expressao:
            if not item.isnumeric():
                a = posfixa.pop()
                b = posfixa.pop()
                posfixa.extend([a, b, item])
            else:
                posfixa.append(item)
        return CalculadoraPosfixa().run(posfixa, operacoes)


class Calculadora:

    def __init__(self, expressao: str):
        self.expressao = expressao
        self._operacoes = {}
        self._set_tipo()
        self.add_operacao('+', Adicao())
        self.add_operacao('-', Subtracao())
        self.add_operacao('*', Multiplicacao())
        self.add_operacao('/', Divisao())
    
    def _set_tipo(self):
        if not self.expressao[0].isnumeric() and self.expressao[0] != '(':
            self.tipo = CalculadoraPrefixa()
        elif not self.expressao[-1].isnumeric():
            self.tipo = CalculadoraPosfixa()
        else:
            self.tipo = CalculadoraInfixa()

    def add_operacao(self, simbolo: str, classe_operacao: Operacao):
        self._operacoes[simbolo] = classe_operacao

    def calcular(self):
        return self.tipo.run(self.expressao.split(), self._operacoes)

    def get_operacao(self, simbolo: str):
        return self._operacoes[simbolo]
