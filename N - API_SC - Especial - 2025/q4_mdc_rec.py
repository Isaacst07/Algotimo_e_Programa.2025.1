# Sábado 
# comecei : 21:40
# parei :  21:55

from q1_number_utils import obter_numero_inteiro_min
from q1_number_utils import limpar_tela


def main():
    num1 = obter_numero_inteiro_min('Digite o primeiro número: ', 1)
    num2 = obter_numero_inteiro_min('Digite o segundo número: ', num1 + 1)

    limpar_tela()

    print(f'Mdc({num2}, {num1} = {mdc(num2, num1)})')


def mdc(num1: int, num2: int):
    resto = num1 % num2

    if resto == 0:
        return f'{num2}'
    else:
        return mdc(num2, resto)
    

main()