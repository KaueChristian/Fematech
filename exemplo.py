def cod_ascii():
    palavra = input('Digite uma senha: ')
    caracteres = list(palavra)
    for caractere in caracteres:
        código = ord(caractere)
        print(código)
    return código

def base_octal(código):
    senha = bin(código)
    senha = senha.strip('0o')
    print( "octal", senha)
    return senha

código = cod_ascii()
base_octal(código)
