import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')

    somatorio = 0 

    for i in range (1, n + 1, 1):
        termo = 1 / i
        somatorio += termo 

    print(f'O valor de S é aproximadamente: {somatorio:.2f}')


main()