import utils


def main():
    numero = input('Digite um número: ')

    utils.limpar_tela()

    print(inteiro_or_decimal(numero))
    

def inteiro_or_decimal(entrada: str):
    if obter_numero_inteiro(entrada) == True:
        return f'{entrada} é um número INTEIRO!'
    elif obter_numero_inteiro(entrada) == False:
        return f'{entrada} é um número DECIMAL!'


def obter_numero_inteiro(entrada):
    
    try:
        int(entrada)
        return True
    except ValueError:
        return False
    

main()