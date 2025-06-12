import utils


def main():
    n = utils.obter_numero_inteiro('N: ')
    lim_inf = utils.obter_numero_inteiro('Limite Inferior: ')
    lim_sup = utils.obter_numero_min_int('Limite Inferior: ', lim_inf+1)

    utils.limpar_tela()

    print(f'Todos os múltiplos de {n} entre os limites lidos são:')

    for i in range (lim_inf, lim_sup+1, 1):
        if i % n == 0:
            print(i)


main()