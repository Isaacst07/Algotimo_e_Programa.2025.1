def main():
    n = int(input())

    for i in range (0, n, 1):
        x, y = map(int, input().split())

        if x > y:
            soma_impares = 0
            for i in range(y + 1, x, 1):
                if i % 2 != 0:
                    soma_impares += i

            print(soma_impares)
            
            soma_impares -= soma_impares
        else:
            soma_impares2 = 0
            for i in range (x + 1, y, 1):
                if i % 2 != 0:
                    soma_impares2 += i

            print(soma_impares2)
            soma_impares2 -= soma_impares2


main()