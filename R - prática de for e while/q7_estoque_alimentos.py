import os 


def main():
    limpar_tela()

    print('Olá, vamos ver a situação do seu estoque!')
    
    dar_espaco()
    itens = obter_numero_int('Quantidade de itens no estoque a analisar: ')
    lista = '----------ESTOQUE DA ISAAC ALIMENTOS----------'

    for i in range (1, itens + 1, 1):
        limpar_tela()
        print(f'-------{i}° ITEM-------')
        nome_alimento = str(input('Nome do alimento: '))
        quantidade = obter_numero_int('Quantidade desse alimento no estoque: ')
        dia_compra, mes_compra, ano_compra = map(int, input('Data da compra do alimento(DD/MM/AAAA): ').split('/'))
        dia_vencimento, mes_vencimento, ano_vencimento = map(str, input('Data de vencimento do alimento(DD/MM/AAAA): ').split('/'))
        input('De enter para o próximo item...')

        total_compra = (ano_compra * 360) + (mes_compra * 12) + dia_compra
        vencimento = (int(ano_vencimento) * 360 ) + (int(mes_vencimento) * 30) + int(dia_vencimento)

        validade = verificar_validade(total_compra, vencimento)

        lista += f'\n{i}° - {nome_alimento}:\n Qunatidade no estoque: {quantidade} \n Data vencimento: {dia_vencimento}/{mes_vencimento}/{ano_vencimento}\n Situação do alimento: {validade}'

    limpar_tela()
    print(lista)


def verificar_validade(total_compra: int, validade: int):
    if validade < total_compra:
        return 'Alimento vencido!'
    else:
        dias_restantes = validade - total_compra
        return f'Alimento dentro do prazo de válidade, falta {dias_restantes} dias para ele alcaçar a data de vencimento!'


def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um inteiro válido!')
        obter_numero_int(label)


def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um inteiro válido!')
        obter_numero_float(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()