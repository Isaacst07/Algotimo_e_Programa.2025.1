def main():
    k = int(input())
    #n, m = map(int, input().split())

    for i in range (0, k, 1):
        coordenadas = map(int, input().split())
        lista_coordenadas = mapear(coordenadas, int)

        if lista_coordenadas == 0:
            break

        
        x = lista_coordenadas[0]
        y = lista_coordenadas[1]

        print(x)
        print(y)


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)


    return nova_colecao


main()