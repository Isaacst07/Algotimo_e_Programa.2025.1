def main():
    numerador = 1
    denominador = 1
    s = 0

    while numerador <= 99 and denominador <= 50:
        s += numerador / denominador
        numerador += 2
        denominador += 1

    print(f'O valor de S é igual a {s:.2f}')


main()