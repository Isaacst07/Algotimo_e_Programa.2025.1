import os


def main():
    qtd_imoveis = obter_numero_int('Quantidade de imóveis para analisar: ')
    maior_retorno_total = 0 
    imovel_retorno_total = None
    maior_retorno_anual = 0 
    imovel_retorno_anual = None
    
    for imovel in range (1, qtd_imoveis + 1, 1):
        limpar_tela()
        print(f'-----------{imovel}° IMÓVEL-----------')
        valor_imovel = obter_numero_float_min('Valor da compra do imóvel: ', 0)
        valor_aluguel = obter_numero_float_min('Valor do aluguel mensal do imóvel: ', 0)
        anos_de_aluguel = obter_numero_float_min('Anos que o imóvel ficou alugado: ', 0)

        valor_total_aluguel = valor_aluguel * (anos_de_aluguel * 12)
        retorno_total = valor_total_aluguel - valor_imovel
        taxa_anualizada = valor_aluguel * 12

        if maior_retorno_total == 0 or retorno_total > maior_retorno_total:
            maior_retorno_total = retorno_total
            imovel_retorno_total = imovel

        if maior_retorno_anual == 0 or taxa_anualizada > maior_retorno_anual:
            maior_retorno_anual = taxa_anualizada
            imovel_retorno_anual = imovel

        limpar_tela()
        print(f'A taxa de retorno anulizada do {imovel}° imóvel é de R$ {taxa_anualizada:.2f} .')
        print(f'E o retorno total do {imovel}° imóvel é de R$ {retorno_total:.2f} .')

        dar_espaco()
        input('Enter to contine...')

    print(f'''------------RESUMO DOS IMÓVEIS------------
a) Imóvel com maior retorno total: {imovel_retorno_total}° imóvel - R$ {maior_retorno_total:.2f}
b) Imóvel com maior taxa de retorno anualizado: {imovel_retorno_anual}° imóvel - R$ {maior_retorno_anual:.2f}

''')


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
        print(f'O valor "{numero}" não está entre o limite minímo {min} e o limite máximo {max}!')
        obter_numero_float_min_max(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()