def main():
    n1, n2, n3, n4 = map(float, (input()).split())

    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

    situacao_aluno(media)


def situacao_aluno(media: float):
    if media >= 7:
        print(f'Media: {media:.1f}')
        print('Aluno aprovado.')
    elif media >= 5:
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        nota_exame = float(input())
        print(f'Nota do exame: {nota_exame:.1f}')
        media_final = (media + nota_exame) / 2
        if media_final >= 5:
            print('Aluno aprovado.')
            print(f'Media final: {media_final:.1f}')
        else:
            print('Aluno reprovado.')
            print(f'Media final: {media_final:.1f}')
    else:
        print(f'Media: {media:.1f}')
        print('Aluno reprovado.')


main()



