import os


def main():
    limpar_tela()
    print('Olá, vamos ajudar você a calcular a quitação da sua dívida!')
    dar_espaco()

    valor_incial = obter_numero_float_min('Valor inicial da sua divida(R$): ', 0)
    taxa_juros = obter_numero_float_min_max('Qual a taxa de juros mensal(%): ', 0, 100)
    qtd_meses = obter_numero_int_min('Quantidade de meses para a quitação: ', 0)

    divida = valor_incial
    mes_quitacao = None

    for mes in range (1, qtd_meses + 1, 1):
        limpar_tela()
        divida *= (1 + (taxa_juros / 100) ** mes)
        print(f'--------{mes}° MÊS--------')
        valor_pagamento = obter_numero_float_min(f'Valor do pagamento(R$): ', 0)

        divida -= valor_pagamento

        if divida <= 0:
            mes_quitacao = mes
            break
        else:
            print(f'O valor da dívida está em R$ {divida:.2f}')
            print(f'Ainda lhe restam {(qtd_meses - mes)} meses para você quita-la.')

        dar_espaco()
        input('Enter to continue ...')

    if mes_quitacao == None:
        limpar_tela()
        print(f'Acabou o tempo de projeção de {qtd_meses} meses que você previu e a divida não foi quitada, faltanda R$ {divida:.2f} .')
    else:
        limpar_tela()
        print(f'Parabéns, você quitou sua dívida no {mes_quitacao}° mês!')
        

def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um interio válido!')
        obter_numero_int(label)


def obter_numero_int_min(label: str, min: int):
    numero = obter_numero_int(label)

    if numero >= min:
        return numero
    else:
        print(f'O valor "{numero}" é menor que o minímo {min}!')
        obter_numero_int_min(label)


def obter_numero_int_min_max(label: str, min: int, max: int):
    numero = obter_numero_int(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'O valor "{numero}" não está entre o limite minímo {min} e o limite máximo {max}!')
        obter_numero_int_min_max(label)
    

def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um numero válido!')
        obter_numero_float(label)


def obter_numero_float_min(label: str, min: int):
    numero = obter_numero_float(label)

    if numero >= min:
        return numero
    else:
        print(f'O valor "{numero}" é menor que o minímo {min}!')
        obter_numero_float_min(label)


def obter_numero_float_min_max(label: str, min: int, max: int):
    numero = obter_numero_float(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'O valor "{numero}" não está entre o limite minímo {min} e o liamite máximo {max}!')
        obter_numero_float_min_max(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()