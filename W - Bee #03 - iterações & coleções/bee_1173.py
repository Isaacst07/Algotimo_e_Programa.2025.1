def main():
    n = []
    valor = int(input())

    for i in range(0, 10, 1):
        n.append(valor)

        print(f'N[{i}] = {n[i]}')

        valor *= 2


main()