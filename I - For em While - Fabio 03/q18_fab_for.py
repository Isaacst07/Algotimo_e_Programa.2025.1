from funcoes import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número N: ')
    numerador = 1
    denominador = n
    s = 0

    while numerador <= n:
        s += numerador / denominador
        numerador += 1
        denominador -= 1

    print(f'O valor de S é igual a {s}')
    

main()