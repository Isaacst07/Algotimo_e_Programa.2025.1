from funcoes import obter_numero_interio_min

def main():
    n = obter_numero_interio_min('Digite um número: ', 2)

    print(f'Os primerios {n} da sequência de Fibonacci são:')

    sequencia_fibo(n)


def sequencia_fibo(numero:int):
    contador = 2 
    numero_a = 0
    numero_b = 1 

    print(numero_a)
    print(numero_b)

    while contador < numero :
        soma = numero_a + numero_b
        numero_a = numero_b 
        contador += 1 
        print(f'{soma}')


main()