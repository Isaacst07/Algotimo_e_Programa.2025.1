import utils


def main():
    lim_inf = utils.obter_numero_inteiro('Limite Inferior: ')
    lim_sup = utils.obter_numero_min_int('Limite Superior: ', lim_inf+1)

    utils.limpar_tela()

    print(f'Os pares entre o limite inferior({lim_inf}) e o limite superior({lim_sup}) são:')

    for i in range (lim_inf, lim_sup+1, 1):
        if i % 2 == 0:
            print(i)

    print('FIM!')


main()