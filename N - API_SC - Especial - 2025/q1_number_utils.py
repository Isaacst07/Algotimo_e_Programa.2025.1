# Sábado
# comecei 12:20
# terminei 12:47

# Domingo:
# voltei para testar as utils: 13:50
# terminei 14:01


import os


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número {entrada} não é um inteiro válido!')
        obter_numero_inteiro(label)


def obter_numero_inteiro_positivo(label: str):
    numero = obter_numero_inteiro(label)

    while True:
        if numero > 0:
            break 
        else:
            print(f'O número {numero} não é um inteiro positivo!')
            return obter_numero_inteiro_positivo(label)
    return numero


def obter_numero_inteiro_negativo(label: str):
    numero = obter_numero_inteiro(label)

    while True:
        if numero < 0:
            break 
        else:
            print(f'O número {numero} não é um inteiro negativo!')
            return obter_numero_inteiro_negativo(label)
    return numero


def obter_numero_inteiro_min(label: str, min: int):
    numero = obter_numero_inteiro(label)

    if numero >= min:
        return numero
    else:
        print(f'O número {numero} digitado está abaixo do minímo permitido {min} !')
        return obter_numero_inteiro_min(label)


def obter_numero_interio_max(label: str, max: int):
    numero = obter_numero_inteiro(label)

    if numero <= max:
        return numero
    else: 
        print(f'O número {numero} digitado está acima do máximo permitido {max} !')
        return obter_numero_interio_max(label)


def obter_numero_inteiro_entre_faixa(label: str, min: int, max: int):
    numero = obter_numero_inteiro(label)

    if numero >= min and numero <= max:
        return numero
    else: 
         print(f'O número {numero} digitado não está entre o mínimo {min} e máximo {max} permitido!')
         return obter_numero_inteiro_entre_faixa(label, min, max)


def obter_float_positivo(label: str):
    numero = float(input(label))

    while True:
        if numero > 0:
            break 
        else:
            print(f'O número {numero} não é positivo!')
            return obter_float_positivo(label)
    return numero
    
    
def limpar_tela():
    os.system('cls')