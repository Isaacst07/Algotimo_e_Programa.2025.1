import utils


def main():
    numero = utils.obter_numero_inteiro('Digite um número positivo ou negativo: ')

    utils.limpar_tela()

    print({eh_positivo_ou_negativo(numero)})
    

def eh_positivo_ou_negativo(numero: int):
    if numero >= 0 :
        return f'Seu número {numero} é POSITIVO!'
    else:
        return f'Seu número {numero} é NEGATIVO!'


main()