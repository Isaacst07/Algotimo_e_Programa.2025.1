# comecei  19:44
# terminei 20:22
# Sábado


from q1_number_utils import obter_numero_inteiro_min
from q1_number_utils import limpar_tela


def main():
    a = obter_numero_inteiro_min('Digite um número: ', 1)
    b = obter_numero_inteiro_min('Digite um número: ', a + 11)
    contador = a 

    limpar_tela()

    print(f'Os números de {a} até {b} e seus divisores são:')

    while contador <= b:
        print(f'{contador} ({divisores(contador)})')

        contador += 1


def divisores(numero: int):
    contador = 1
    divisores = 0

    while contador <= numero:

        if numero % contador == 0:
                divisores += 1
        contador += 1

    if numero == 1:
         return '1'
    else:
        return f'{divisores}'

    
main()
