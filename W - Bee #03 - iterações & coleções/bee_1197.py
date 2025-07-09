def main():
    while True:

        try:
            entrada = map(str, input().split())
            lista = mapear(entrada, str)

            v = int(lista[0])
            t = int(lista[1])

            dobro_deslocamento = (v * t) * 2

            print(dobro_deslocamento)
            
        except EOFError:
            break             


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)


    return nova_colecao


main()