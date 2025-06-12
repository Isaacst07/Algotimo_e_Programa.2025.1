from funcoes import obter_numero_inteiro
from funcoes import obter_numero_interio_min

def main():

    n = obter_numero_inteiro('N: ')
    limite_inf = obter_numero_interio_min('Qual o limite inferior: ', 0)
    limite_sup = obter_numero_interio_min('Qual o limite superior: ', limite_inf + 1)

    obter_multiplos(n, limite_inf, limite_sup)


def obter_multiplos(n, limite_inf, limite_sup):
    multiplo = limite_inf

    print(f'Os multiplos de {n} entre {limite_sup} e {limite_inf} são: ')
    
    while multiplo <= limite_sup:
        if multiplo % n == 0:
            print(f'{multiplo}')

        multiplo += 1 

    
main()