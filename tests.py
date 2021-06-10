import unittest

from calculadora import Calculadora
from estacionamento import Estacionamento, Carro, Moto


class CalculadoraTestCase(unittest.TestCase):

    # CALCULADORA INFIXA
    def test_calcularora_infixa_adicao(self):
        expressao = Calculadora('10 + 10')
        self.assertEqual(expressao.calcular(), 20)

    def test_calcularora_infixa_subtracao(self):
        expressao = Calculadora('10 - 10')
        self.assertEqual(expressao.calcular(), 0)

    def test_calcularora_infixa_multiplicacao(self):
        expressao = Calculadora('10 * 10')
        self.assertEqual(expressao.calcular(), 100)

    def test_calcularora_infixa_divisao(self):
        expressao = Calculadora('10 / 10')
        self.assertEqual(expressao.calcular(), 1)

    # CALCULADORA PREFIXA
    def test_calcularora_prefixa_adicao(self):
        expressao = Calculadora('+ 10 10')
        self.assertEqual(expressao.calcular(), 20)

    def test_calcularora_prefixa_subtracao(self):
        expressao = Calculadora('- 10 10')
        self.assertEqual(expressao.calcular(), 0)

    def test_calcularora_prefixa_multiplicacao(self):
        expressao = Calculadora('* 10 10')
        self.assertEqual(expressao.calcular(), 100)

    def test_calcularora_prefixa_divisao(self):
        expressao = Calculadora('/ 10 10')
        self.assertEqual(expressao.calcular(), 1)

    # CALCULADORA POSFIXA
    def test_calcularora_posfixa_adicao(self):
        expressao = Calculadora('10 10 +')
        self.assertEqual(expressao.calcular(), 20)

    def test_calcularora_posfixa_subtracao(self):
        expressao = Calculadora('10 10 -')
        self.assertEqual(expressao.calcular(), 0)

    def test_calcularora_posfixa_multiplicacao(self):
        expressao = Calculadora('10 10 *')
        self.assertEqual(expressao.calcular(), 100)

    def test_calcularora_posfixa_divisao(self):
        expressao = Calculadora('10 10 /')
        self.assertEqual(expressao.calcular(), 1)
    
    def test_multiplas_operacoes(self):
        expressao = Calculadora('10 + 10 * 10 - 5')
        self.assertEqual(expressao.calcular(), 105)


class TestEstacionamento(unittest.TestCase):

    def setUp(self):
        self.estacionamento = Estacionamento(andar=3, vagas_por_andar=4)

    def test_estacionar_carro(self):
        carro = Carro('gol')
        esperado = [
            ["Carro('gol')", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
        ]
        resultado = self.estacionamento.estacionar(carro)
        self.assertEqual(resultado, esperado)
    
    def test_estacionar_varios_carros(self):
        carro = Carro('gol')
        self.estacionamento.estacionar(carro)
        resultado = self.estacionamento.estacionar(
            Carro('fusca'),
            Carro('santana'),
            Carro('premium'),
            Carro('tempra')
        )
        esperado = [
            ["Carro('gol')", "Carro('fusca')", "Carro('santana')", "Carro('premium')"],
            ["Carro('tempra')", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
        ]
        self.assertEqual(resultado, esperado)

    def test_estacionar_moto(self):
        moto = Moto('cg')
        esperado = [
            ["Moto('cg')", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
        ]
        resultado = self.estacionamento.estacionar(moto)
        self.assertEqual(resultado, esperado)
    
    def test_estacionar_varias_motos(self):
        esperado = [
            ["Moto('cg'), Moto('dt')", "Moto('custom')", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
        ]
        resultado = self.estacionamento.estacionar(Moto('cg'), Moto('dt'), Moto('custom'))
        self.assertEqual(resultado, esperado)
    
    def test_estacionar_carros_e_motos(self):
        esperado = [
            ["Carro('gol')", "Moto('cg'), Moto('dt')", "Carro('santana')", "Moto('custom')"],
            ["vazia", "vazia", "vazia", "vazia"],
            ["vazia", "vazia", "vazia", "vazia"],
        ]
        resultado = self.estacionamento.estacionar(
            Carro('gol'),
            Moto('cg'),
            Carro('santana'),
            Moto('dt'),
            Moto('custom')
        )
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
