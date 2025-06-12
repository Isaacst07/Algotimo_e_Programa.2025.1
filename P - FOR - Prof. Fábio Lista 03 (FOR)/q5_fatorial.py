import utils


def main():
    numero = utils.obter_numero_inteiro('Digite um número: ')

    utils.limpar_tela()

    print(f'O {numero}! é igual a:')

    for i in range(numero-1 , 1, -1):
        numero *= i 

    print(numero)

main()