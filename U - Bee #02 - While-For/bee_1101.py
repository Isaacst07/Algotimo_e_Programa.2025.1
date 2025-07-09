def main():

    while True:

        n, m = map(int, input().split())

        if n <= 0 or m <= 0:
            break
        
        if m > n :
            m ,n = n, m

        soma = 0
        numeros = ''

        for i in range (m, n + 1, 1):
            soma += i
            numeros += f'{i} '
        numeros += f'Sum={soma}'
        print(numeros)

        
main()