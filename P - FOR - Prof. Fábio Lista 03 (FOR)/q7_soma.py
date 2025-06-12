import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')

    utils.limpar_tela()

    print(f'A soma dos interios de 1 até {n} é igual a:')

    for i in range(n-1 , 0, -1):
        n += i 

    print(n)
        

main()