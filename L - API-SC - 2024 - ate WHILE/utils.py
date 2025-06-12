import os

def obter_numero_real(label: str):
    return float(input(label))


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número {entrada} não é um inteiro válido')
        return obter_numero_inteiro(label)
    

def obter_numero_min(label: str, min: int):
    numero = obter_numero_inteiro(label)

    if numero <= min :
        return numero
    else:
        print(f'O número {numero} é menor que o mínimo {min}')
        return obter_numero_inteiro(label, min)
    

def obter_numero_entre(label: str, min: float, max: float):
    numero = obter_numero_real(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'O número {numero} não está dentro da faixa miníma {min} e da faixa máxima {max}')
        return obter_numero_inteiro(label, min)
    

def limpar_tela():
    os.system('cls')


def obter_nome(label: str):
    return str(input(label))

   
        