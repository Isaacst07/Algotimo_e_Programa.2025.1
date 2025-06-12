import utils 


def main():
    nota_1 = utils.obter_numero_real('Digite a primeira nota do aluno: ')
    nota_2 = utils.obter_numero_real('Digite a segunda nota do aluno: ')

    utils.limpar_tela()

    situacao_media(nota_1, nota_2)


def situacao_media(nota_1: float, nota_2: float):
    media = (nota_1 + nota_2) / 2 

    if media == 10:
        return print(f'Sua média foi {media:.1f}, então o aluno foi APROVADO COM DISTINÇÃO!')
    elif media >= 7:
        return print(f'Sua média foi {media:.1f}, então o aluno foi APROVADO!')
    else:
         return print(f'Sua média foi {media:.1f}, então o aluno foi REPROVADO!')
    

main()