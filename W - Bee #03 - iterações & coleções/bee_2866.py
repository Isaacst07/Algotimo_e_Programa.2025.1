def main():
    c =  int(input())

    for i in range (0, c, 1):
        mensagem = input()
        mensagem_extraida = ''

        for letra in mensagem:
            if ord(letra) >= 97 and ord(letra) <= 122:
                mensagem_extraida += f'{letra}'

        mensagem_invertida = inverte(mensagem_extraida)
        print(mensagem_invertida)


def inverte(palavra):
    return palavra[::-1]


main()