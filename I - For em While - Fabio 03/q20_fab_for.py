from funcoes import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número N: ')
    denominador = 1
    s = 0
    sinal = 1

    while denominador <= n:
        s += sinal * (1 / denominador)
        sinal *= -1
        denominador += 1

    print(f'O valor de S é igual a {s:.2f}')


main()