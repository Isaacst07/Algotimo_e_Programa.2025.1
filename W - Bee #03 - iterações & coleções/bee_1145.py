def main():
    x, y = map(int, input().split())
    saida = ''

    for i in range (1, y + 1, 1):
        
        if i % x == 0:
                saida += f'{i}'
                print(saida)
                saida = ''
        else:
                saida += f'{i} '


main()