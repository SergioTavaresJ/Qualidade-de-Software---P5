import unittest
import math

# Funções da calculadora
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero não permitida"
    return x / y

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial não definido para números negativos"
    return math.factorial(x)

def potencia(x, y):
    return x ** y

# Testes unitários
class TestCalculadora(unittest.TestCase):

    def test_adicao(self):
        self.assertEqual(adicao(10, 5), 15)
        self.assertEqual(adicao(-1, 1), 0)
        self.assertEqual(adicao(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 5), 5)
        self.assertEqual(subtracao(-1, 1), -2)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicacao(10, 5), 50)
        self.assertEqual(multiplicacao(-1, 1), -1)
        self.assertEqual(multiplicacao(0, 100), 0)

    def test_dividir(self):
        self.assertEqual(divisao(10, 5), 2)
        self.assertEqual(divisao(-10, 2), -5)
        self.assertEqual(divisao(10, 0), "Erro: Divisão por zero não permitida")

    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(-1), "Erro: Fatorial não definido para números negativos")

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(10, 0), 1)
        self.assertEqual(potencia(5, -1), 0.2)

# Execução dos testes
if __name__ == '__main__':
    unittest.main()
