import os
import time


def obter_numero_real(label: str):
    return float(input(label))


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número digitado "{entrada}" não é um inteiro válido!')
        obter_numero_inteiro(label)


def obter_numero_inteiro_min(label: str, min: int):
    numero = obter_numero_inteiro(label)

    if numero <= min:
        return numero
    else: 
        print(f'O número digitado "{numero}" ultrapassa o minímo {min}!')
        obter_numero_inteiro_min(label, min)


def obter_numero_entre_int(label: str, min: int, max: int):
    numero = obter_numero_inteiro(label)

    if numero <= max and  numero >= min:
        return numero
    else:
        print(f'O número digitado "{numero}" não está entre o mínimo {min} e o máximo {max} !')
        obter_numero_entre_int(label, min, max)


def obter_numero_entre_float(label: str, min: int, max: int):
    numero = obter_numero_real(label)

    if numero <= max and  numero >= min:
        return numero
    else:
        print(f'O número digitado "{numero}" não está entre o mínimo {min} e o máximo {max} !')
        obter_numero_entre_int(label, min, max)


def limpar_tela():
    os.system('cls')


def obter_string(label: str):
    return str(input(label))


def dar_espaco():
    print('')


def esperar(duracao: int):
    tempo = duracao / 1000
    time.sleep(tempo)


