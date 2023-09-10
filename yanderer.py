import random
import math
import sympy as sp

# Instruções: a função encrip já funciona para a conversão de números usando bases de números com ponto flutuante, resta programar
# a função para gerar a base de conversão usando a função de limite cuja a função será F(y) = (x + 3 ** (1/2))**2.
# (Z é igual ao limite de F(y) quando X tende a O) onde Z é a  base que será usada para conversão, y é a posição do algarismo que será convertido,
# X é o algarismo que será convertido e O é o número máximo da base que estará sendo utilizada.

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
        valor = []
    
    # Realiza a conversão dos caracteres para as bases geradas usando o método da divisão
        while(i != 0):
            valor.append(str(i % base))
            i = i // base
        indice.append(' '.join(map(str,valor[::-1])))
    
    # Separa cada conjunto de algarismos referentes aos mesmos caracteres em listas individuais e as guarda na lista resultado
    for j in indice:
        val = j.split()
        resultado.append(val)

    return baseval, resultado # Retorna uma tupla com duas listas, uma contem as bases usadas para conversão em cada caractere
                              # a outra contem uma as listas com os números individuais para cada caractere

# função de desencriptação
def deencrip(entrada, bases):
    corda = []
    # acessa cada lista (valor de caracter) presente na lista entrada
    for num,char in enumerate(entrada):
        calcu = 0
    
    # acessa cada número individual da lista filha para realizar a desconversão usando a base correspondente
        for posix,valor in enumerate(char[::-1]):
            calcu += float(valor)*(bases[num]**posix)
        corda.append(calcu)
    
    return corda #retorna uma lista com os valores ascii correspondentes aos caracteres da string inserida inicialmente em formato float
    
