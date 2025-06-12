import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')
    soma_num = 0 

    utils.limpar_tela()

    for i in range (1, n+1, 1):
        numero = utils.obter_numero_inteiro('Número da lista N: ')
        soma_num += numero

    utils.limpar_tela()

    print(f'''------RELATÓRIO DA LISTA------
a) Soma dos números da lista: {soma_num}
b) A média dos números da lista: {(soma_num / n):.2f}       
''')


main()