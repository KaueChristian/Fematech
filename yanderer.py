import random
import math
import sympy as sp

def convert(corda):
    # só transforma a string recebida nos seus respectivos valores em ascii
    chars = map(ord, list(str(corda)))

    baseval = []
    resultado = []
    indice = []
    
    # Definição da função limite
    # X = sp.Symbol('X')
    # funcao = (X + 2)**2
    
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
def taylors(func, Cvalue):
    result = 0
    for n in range(0, 10):
        calculo = ((sp.diff(func.subs(sp.symbols('x'), Cvalue), sp.symbols('x'), n)) / math.factorial(n)) * (sp.symbols('x') - Cvalue)**n
        result += calculo
    return result


def calculus (func):
    result = 0
    for n in range(0, 10):
        calculo = ((sp.diff(func.subs(sp.symbols('x'), 0), sp.symbols('x'), n)) / math.factorial(n)) * (sp.symbols('x'))**n
        result += calculo
    return result