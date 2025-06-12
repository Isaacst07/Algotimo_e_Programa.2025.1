import utils 


def main():
    n = utils.obter_numero_inteiro('Digite um número inteiro: ')

    utils.limpar_tela()

    print(f'Todos os pares entre 1 e {n} são:')

    for i in range (2, n+1, 2):
        print(i)


main()