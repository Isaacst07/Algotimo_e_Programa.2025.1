import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')
    soma = 0

    print('Os n primeiros termos das sequência são:')

    for i in range (1, n + 1):
        soma += i
        print(soma)


main()