import math

import sympy as sp

import yanderer

# teste 1
bases, valores = yanderer.convert(12345678)
# print(bases)
# print(valores)
# print(yanderer.deencrip(valores, bases))
x = sp.symbols('x')
funcao = sp.sin(x)

print(yanderer.taylors(4,funcao))
print(yanderer.MacLaurin(funcao))
# print(yanderer.teste(yanderer.taylors(8,4,funcao),yanderer.MacLaurin(4,funcao)))