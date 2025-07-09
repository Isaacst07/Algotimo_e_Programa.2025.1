def main():
    while True:

        try:
            n = int(input())
            cod_livros = []

            for i in range (0, n, 1):
                entrada = input()
                cod_livros.append(entrada)

            livros_ordenados = ordenar(cod_livros)

            for livro in livros_ordenados:
                print(livro)

        except EOFError:
            break
                

def ordenar(lista):
    n = len(lista)

    for i in range(0, n, 1):

        for j in range(0, n - i - 1, 1):

            if int(lista[j]) > int(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


main()