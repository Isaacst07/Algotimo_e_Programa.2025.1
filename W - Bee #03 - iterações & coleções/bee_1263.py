def main():
        while True:
            try:
                 linha = input()

                 print(contar_aliteracoes(linha))

            except EOFError:
                 break


def contar_aliteracoes(linha):
    palavras = linha.strip().split()
    aliteracoes = 0
    i = 0
    n = len(palavras)

    while i < n:
        letra_atual = palavras[i][0].lower()
        grupo_tamanho = 1

        for j in range(i + 1, n):
            if palavras[j][0].lower() == letra_atual:
                grupo_tamanho += 1
            else:
                break

        if grupo_tamanho > 1:
            aliteracoes += 1

        i += grupo_tamanho  

    return aliteracoes


main()