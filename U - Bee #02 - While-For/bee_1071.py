def main():
    x = int(input())
    y = int(input())
    soma_impares = 0

    for i in range (y + 1, x , 1):
        print(i)
        if i % 2 != 0:
            soma_impares += i

    print(soma_impares)


main()