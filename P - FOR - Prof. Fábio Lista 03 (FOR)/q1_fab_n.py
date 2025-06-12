import utils


def main():
    n = utils.obter_numero_inteiro('Digite um número inteiro: ')

    utils.limpar_tela()

    print(f'Todos números entre 1 e {n} são:')

    for i in range (1, n+1, 1):
        print(i)


main()