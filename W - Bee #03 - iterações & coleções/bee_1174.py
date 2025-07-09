def main():
    valores = []

    for i in range(0, 100, 1):
        valor = float(input())
        valores.append(valor)

        if valores[i] <= 10:
            print(f'A[{i}] = {valores[i]}')


main()