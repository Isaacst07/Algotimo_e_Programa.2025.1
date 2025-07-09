def main():
    N = []

    for i in range (0, 20, 1):
        valor = int(input())
        N.append(valor)

    N_invertido = inverte_valores(N)

    for j in range (0, 20, 1):
        print(f'N[{j}] = {N_invertido[j]}')


def inverte_valores(lista):
    ultimo_vetor = 19

    for x in range(0, 10, 1):
        lista[x], lista[ultimo_vetor] = lista[ultimo_vetor], lista[x]
        ultimo_vetor -= 1

    return lista


main()