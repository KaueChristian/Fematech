import yanderer
import math
import sympy as sp

# teste 1
# bases, valores = yanderer.convert(12345678)
# print(bases)
# print(valores)
# print(yanderer.deencrip(valores, bases))

x = sp.symbols('x')
funcao = (x+2)**2

resultado = yanderer.calculus(funcao)
print(resultado)
