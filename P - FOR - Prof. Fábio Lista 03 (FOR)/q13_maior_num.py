import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')
    maior_num = 0 

    utils.limpar_tela()

    for i in range (1, n+1, 1):
        numero = utils.obter_numero_inteiro('Número da lista N: ')
        
        if maior_num == 0 or numero > maior_num:
            maior_num = numero

    utils.limpar_tela()

    print(f'O maior número da lista é o: {maior_num}')


main()