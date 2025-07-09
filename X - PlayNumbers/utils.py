import os  


def limpar_tela():
    os.system('cls')


def chamar_menu():
    limpar_tela()

    menu = '''\t>>>>>>>Play Numbers<<<<<<
        1 - Mostar Todos os valores
        2 - Resetar Vetor
        3 - Quantidade de itens no Vetor
        4 - Ver Menor e Maior valores e suas posições
        5 - Somatório
        6 - Média de valores
        7 - Mostrar positivos e sua quantidade
        8 - Mostrar negativos e sua quantidade
        9 - Atualizar Valores por uma regra
        10 - Adiconar Novo Valor
        11 - Remover Itens por Valor exato
        12 - Remover por Posição
        13 - Editar valor específico por posição
        14 - Salvar valores em arquivo

        0 - sair

        >>> '''

    opcao = obter_numero_da_faixa(menu, 0, 15)

    return opcao


def regra_opcao_9():
    menu3 = '''=============== Qual a regra para atualizar valor ===============
        1 - Multiplicar por um valor
        2 - Elevar a um valor (Exponenciação)
        3 - Reduzir a uma fração
        4 - Substituir valores negativos por um número aleatórios da uma faixa(min, max)
        5 - Ordenar valores
        6 - Embaralhar Valores

        >>> '''
            
    regra = obter_numero_da_faixa(menu3, 1, 6)

    return regra


def obter_numero_inteiro(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        
    except ValueError:
        print(f'O número digitado {entrada} não é um inteiro válido!')
        numero = obter_numero_inteiro(label)

    return numero


def obter_numero_positivo(label: str):
    while True:
        numero = obter_numero_inteiro(label)

        if numero >= 0:
            break
        else:
            print(f'O número digitado {numero} não é positivo!')
            obter_numero_positivo(label)

    return numero


def obter_numero_negativo(label: str):
    while True:
        numero = obter_numero_inteiro(label)

        if numero < 0:
            break
        else:
            print(f'O número digitado {numero} não é negativo!')
            obter_numero_positivo(label)
    
    return numero


def obter_numero_minimo(label: str, min):
    while True:
        numero = obter_numero_inteiro(label)

        if numero >= min:
            break
        else:
            print(f'Número fora da faixa miníma {min}!')
            obter_numero_minimo(label, min)

    return numero


def obter_numero_da_faixa(label: str, min: int,max: int):
    numero = obter_numero_inteiro(label)

    while numero < min or numero > max:
        print(f'Número fora da faixa {min} minimo {max} maximo')
        numero = obter_numero_da_faixa(label, min, max)

    return numero


def somar(valor1, valor2):
    return valor1 + valor2


def finalizar():
    input('Enter to continue... ')
    limpar_tela()