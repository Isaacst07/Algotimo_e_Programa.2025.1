from funcoes import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite o valor de N: ')
    numerador = 1
    S = 0

    while numerador <= n:
        S += 1 / numerador
        numerador += 1

    print(f'O valor de S é igual a {S:.2f}')


main()