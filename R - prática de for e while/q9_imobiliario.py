import os


def main():
    limpar_tela()
    print('Olá, vamos te ajudar na compra do seu imóvel!')
    dar_espaco()

    valor_imovel = obter_numero_float_min('Valor do imóvel(R$): ', 0)
    valor_entrada = obter_numero_float_min('Valor da entrada(R$): ', 0)
    taxa_juros = obter_numero_float_min_max('Qual a taxa de juros mensal(%): ', 0, 100)
    qtd_parcelas = obter_numero_int_min('Quantidade de meses para a quitação: ', 0)

    pagamento_imovel = (valor_imovel - valor_entrada) * ((1 + (taxa_juros / 100)) ** qtd_parcelas)
    valor_parcela = pagamento_imovel / qtd_parcelas
    juros_parcela = pagamento_imovel * (taxa_juros / 100)

    limpar_tela()

    for parcela in range (1, qtd_parcelas + 1, 1):
        
        pagamento_imovel -= valor_parcela
    
        print(f'''--------{parcela}° PARCELA--------
a) Valor da parcela: R$ {valor_parcela:.2f}
b) Juros da parcela: R$ {juros_parcela:.2f}
c) Saldo devedor após parcela: R$ {pagamento_imovel:.2f} 
    ''')

    print('Fim')
       
        
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