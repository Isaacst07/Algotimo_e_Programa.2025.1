import os 


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    
    except ValueError:
        print(f'O número "{entrada}" não é um número válido!')
        return obter_numero_inteiro(label)


def obter_numero_da_faixa(label: str, min: int, max: int):
    numero = obter_numero_inteiro(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'Número fora da faixa {min} e {max}')
        return obter_numero_da_faixa(label, min, max)


def obter_numero_minimo(label: str, min: int):
    numero = obter_numero_inteiro(label)

    while numero < min:
        print(f'Número menor que o mínimo {min}!')
        return obter_numero_minimo(label, min)

    return numero 


def limpar_tela():
    os.system('cls')


def finalizar():
    print()
    input('Enter to continue... ')
    limpar_tela()


def dar_espaco():
    print()