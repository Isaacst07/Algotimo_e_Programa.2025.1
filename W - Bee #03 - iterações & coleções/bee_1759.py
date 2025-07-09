def main():
    n = int(input())
    saida = ''

    for i in range (0, n, 1):
        if i == (n - 1):
            saida += 'Ho!'
        else:
            saida += 'Ho '

    print(saida)


main()