import utils

def main():
    n = utils.obter_numero_min_int('N: ', 2)

    print(f'Os primerios {n} da sequência de Fibonacci são:')

    x = 0 
    y = 1 

    for i in range (n):
        print(x)
        proximo = x + y
        x = y 
        y = proximo 


main()