def main():
    movimentos = int(input())
    moeda_posicao = input()

    posicao = posicao_da_moeda(movimentos, moeda_posicao)
    print(posicao)


def posicao_da_moeda(movimentos: int, moeda_posicao: str):

    for i in range (movimentos):
        tipo_movimento = int(input())

        if tipo_movimento == 1:
            if moeda_posicao == 'A':
                moeda_posicao = 'B'
            elif moeda_posicao == 'B':
                moeda_posicao = 'A'
        elif tipo_movimento == 2:
            if moeda_posicao == 'B':
                moeda_posicao = 'C'
            elif moeda_posicao == 'C':
                moeda_posicao = 'B'
        elif tipo_movimento == 3:
            if moeda_posicao == 'A':
                moeda_posicao = 'C'
            elif moeda_posicao == 'C':
                moeda_posicao = 'A'

    return moeda_posicao


main()