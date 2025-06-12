import utils 


def main():
    a0 = utils.obter_numero_inteiro('Digite o A0 da progressão aritmética: ')
    limite = utils.obter_numero_inteiro('Limite da progressão aritmética: ')
    r = utils.obter_numero_inteiro('Razão da progressão aritmética: ')

    utils.limpar_tela()

    print(f'Os valores menores que o limite {limite} são:')

    for i in range (a0, limite, r):
        print(i)


main()