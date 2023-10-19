import random
import math
import sympy as sp

def convert(corda):
    # só transforma a string recebida nos seus respectivos valores em ascii
    chars = map(ord, list(str(corda)))

    baseval = []
    resultado = []
    indice = []
    
    # Gera numeros aleatórios que serão as bases de conversão para cada caracter presente na string
    for i in chars:
        base = random.uniform(2.0, 10.0) # 10 > base >= 2
        baseval.append(base)

    # Realiza a conversão dos caracteres para as bases geradas usando o método da divisão
        valor = []
        while(i != 0):
            valor.append(str(i % base))
            i = i // base
        indice.append(' '.join(map(str,valor[::-1])))
    
    # Separa cada conjunto de algarismos referentes aos mesmos caracteres em listas individuais e as guarda na lista resultado
    for j in indice:
        val = j.split()
        resultado.append(val)

    return baseval, resultado # Retorna uma tupla com duas listas, uma contem as bases usadas para conversão em cada caractere
                              # a outra contem as listas com os números individuais para cada algarismo dos numeros convertidos

# função de desencriptação
def deencrip(entrada, bases):
    corda = []
    # acessa cada lista (valor de caracter) presente na lista entrada
    for num,char in enumerate(entrada):
        calc = 0
    
    # acessa cada número individual da lista filha para realizar a desconversão usando a base correspondente
        for posix,valor in enumerate(char[::-1]):
            calc += float(valor)*(bases[num]**posix)
        corda.append(chr(int(calc)))
    
    return corda #retorna uma lista com os valores ascii correspondentes aos caracteres da string inserida inicialmente em formato float
    
#função pra calcular o polinomio de taylor, recebe como argumentos a função matemática na qual se deseja calcular o polinomio
#e Cvalue que representa o ponto no plano cartesiano em torno do qual se da o cálculo
#nem tenta entender o que ta escrito pq nem eu entendi direito ksksksks o importante e que essa função atuará como chave privada
def taylors(Cvalue,func):
    terms = []
    x = sp.symbols('x')
    for n in range(0, 50):
        fX = sp.diff(func, x, n)
        calculo = (fX.subs(x,Cvalue) / math.factorial(n)) * (x - Cvalue)**n
        terms.append(calculo)
    return terms

def MacLaurin (func):
    result = []
    x = sp.symbols('x')
    for n in range(0, 50):
        fX = sp.diff(func, x, n)
        calculo = (fX.subs(x,0) / math.factorial(n)) * (x ** n)
        result.append(calculo)
    return result

def teste(taylor,mac):
  checklist = []
  for item in mac:
    for n in taylor:
      if abs(item - n) < 1e-97:
        checklist.append(True)
      else: 
        checklist.append(False)
  return checklist

# def calculus(bases):
#    for item in bases:
      