def main():
    n = int(input())

    for i in range (0, n, 1):
        x, y = map(int, input().split())

        if y == 0:
            print('divisao impossivel')
        else:
            divisao = x / y
            print(f'{divisao:.1f}')


main()