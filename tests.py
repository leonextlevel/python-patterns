import unittest

from calculadora import Calculadora


class CalculadoraTestCase(unittest.TestCase):

    # CALCULADORA INFIXA
    def test_calcularora_infixa_adicao(self):
        expressao = Calculadora('10 + 10')
        self.assertEquals(expressao.calcular(), 20)

    def test_calcularora_infixa_subtracao(self):
        expressao = Calculadora('10 - 10')
        self.assertEquals(expressao.calcular(), 0)

    def test_calcularora_infixa_multiplicacao(self):
        expressao = Calculadora('10 * 10')
        self.assertEquals(expressao.calcular(), 100)

    def test_calcularora_infixa_divisao(self):
        expressao = Calculadora('10 / 10')
        self.assertEquals(expressao.calcular(), 1)

    # CALCULADORA PREFIXA
    def test_calcularora_prefixa_adicao(self):
        expressao = Calculadora('+ 10 10')
        self.assertEquals(expressao.calcular(), 20)

    def test_calcularora_prefixa_subtracao(self):
        expressao = Calculadora('- 10 10')
        self.assertEquals(expressao.calcular(), 0)

    def test_calcularora_prefixa_multiplicacao(self):
        expressao = Calculadora('* 10 10')
        self.assertEquals(expressao.calcular(), 100)

    def test_calcularora_prefixa_divisao(self):
        expressao = Calculadora('/ 10 10')
        self.assertEquals(expressao.calcular(), 1)

    # CALCULADORA POSFIXA
    def test_calcularora_posfixa_adicao(self):
        expressao = Calculadora('10 10 +')
        self.assertEquals(expressao.calcular(), 20)

    def test_calcularora_posfixa_subtracao(self):
        expressao = Calculadora('10 10 -')
        self.assertEquals(expressao.calcular(), 0)

    def test_calcularora_posfixa_multiplicacao(self):
        expressao = Calculadora('10 10 *')
        self.assertEquals(expressao.calcular(), 100)

    def test_calcularora_posfixa_divisao(self):
        expressao = Calculadora('10 10 /')
        self.assertEquals(expressao.calcular(), 1)
    
    def test_multiplas_operacoes(self):
        expressao = Calculadora('10 + 10 * 10 - 5')
        self.assertEquals(expressao.calcular(), 105)


if __name__ == '__main__':
    unittest.main()
