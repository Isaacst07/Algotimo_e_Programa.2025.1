def main():
    n = int(input("Digite o valor de N: "))
    numerador = 1
    denominador = n
    s = 0
    sinal = 1

    while denominador >= 1:
        s += sinal * (numerador / denominador)
        numerador += 2
        denominador -= 1
        sinal *= -1  

    print(f'O valor de S é igual a {s:.2f}')


main()