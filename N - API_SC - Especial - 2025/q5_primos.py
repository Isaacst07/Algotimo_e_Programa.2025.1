# Sábado:
# comecei 12:50 
# terminei 13:20
# parei fui para o curso

from q1_number_utils import obter_numero_inteiro_min
from q1_number_utils import limpar_tela


def main():
    n = obter_numero_inteiro_min('Digite um número: ', 1)
    m = obter_numero_inteiro_min('Digite um número maior que o anterior: ', n + 1)
    

    limpar_tela()

    print(f'Os primos e não primos entre {n} e {m} são:')

    while n <= m:
        print(f'{n} - {eh_primo(n)}')
        n += 1


def eh_primo(numero: int):
    contador = 2
    divisores = 0

    while contador <= numero:
            if numero % contador == 0:
                divisores += 1
            contador += 1

    if numero == 1:
        return 'Não é primo'
    if 0 < divisores and divisores < 2:
        return 'É primo'
    else:
        return 'Não é primo'
        

main()
    