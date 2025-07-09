def main():
    maior_valor = 0
    posicao = 0

    for i in range (1, 101, 1):
        x = int(input())

        if x > maior_valor:
            maior_valor = x
            posicao = i

    print(f'{maior_valor}\n{posicao}')


main()