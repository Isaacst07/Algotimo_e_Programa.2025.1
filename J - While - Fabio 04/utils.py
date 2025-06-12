import os 

def obter_numero_real(label: str):
    return float(input(label))


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número {numero} não é um inteiro válido!')
        obter_numero_inteiro(label)

def limpar_tela():
    os.system('cls')