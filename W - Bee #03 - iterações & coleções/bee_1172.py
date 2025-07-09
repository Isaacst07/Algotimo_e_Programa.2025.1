def main():
    x = []
    for i in range (0, 10, 1):
        valor = int(input())
        x.append(valor)

        if x[i] == 0 or x[i] < 0:
            x[i] = 1

        print(f'X[{i}] = {x[i]}')


main()