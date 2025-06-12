import os

def obter_numero_real(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número digitado "{entrada}" não é válido!')
        obter_numero_real(label)


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número digitado "{entrada}" não é um interio válido!')
        obter_numero_real(label)


def obter_numero_min_int(label: str, min: int):
    numero = obter_numero_inteiro(label)

    if numero >= min:
        return numero
    else:
        print(f'O número digitado "{numero}" ultrapassa o mínimo !')


def limpar_tela():
    os.system('cls')

