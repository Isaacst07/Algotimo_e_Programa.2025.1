import utils


def main():
    produto1 = utils.obter_numero_real('Valor do primeiro produto: ')
    produto2 = utils.obter_numero_real('Valor do segundo produto: ')
    produto3 = utils.obter_numero_real('Valor do terceiro produto: ')

    utils.limpar_tela()

    mais_barato(produto1, produto2, produto3)


def mais_barato(produto1: float, produto2: float, produto3: float):
    if produto1 > produto2 and produto1 > produto3:
        return print(f'O produto mais barato é produto 1 R$ {produto1:.2f} .')
    elif produto2 > produto1 and produto2 > produto3:
        return print(f'O produto mais barato é produto 2 R$ {produto3:.2f} .')
    elif produto3 > produto1 and produto3 > produto2:
        return print(f'O produto mais barato é produto 3 R$ {produto3:.2f} .')
    else: produto1 == produto2 and produto1 == produto3
    return print(f'Os produto tem mesmo preço R$ {produto1:.2f} tanto faz comprar qualquer um!')


main()