import utils 


def main():
    utils.limpar_tela()

    print('Olá, vamos calcular a média de um aluno para você!')

    utils.dar_espaco()

    nota1 = utils.obter_numero_entre_float('1° nota do aluno: ', 0, 10)
    nota2 = utils.obter_numero_entre_float('2° nota do aluno: ', 0, 10)

    utils.limpar_tela()

    print(media(nota1, nota2))


def media(nota1: float, nota2: float):
    media = (nota1 + nota2) / 2

    if media >= 9:
        resumo = f'''------------SITUAÇÃO DO ALUNO------------
a) 1° nota do aluno: {nota1:.1f}
b) 2° nota do aluno: {nota2:.1f}
c) Média do aluno  : {media:.1f}
d) Conceito        : A

O aluno foi APROVADO!
        '''
        return resumo
    
    elif media >= 7.5:
        resumo = f'''------------SITUAÇÃO DO ALUNO------------
a) 1° nota do aluno: {nota1:.1f}
b) 2° nota do aluno: {nota2:.1f}
c) Média do aluno  : {media:.1f}
d) Conceito        : B

O aluno foi APROVADO!
        '''
        return resumo
    
    elif media >= 6:
        resumo = f'''------------SITUAÇÃO DO ALUNO------------
a) 1° nota do aluno: {nota1:.1f}
b) 2° nota do aluno: {nota2:.1f}
c) Média do aluno  : {media:.1f}
d) Conceito        : C

O aluno foi APROVADO!
        '''
        return resumo
    
    elif media >= 4:
        resumo = f'''------------SITUAÇÃO DO ALUNO------------
a) 1° nota do aluno: {nota1:.1f}
b) 2° nota do aluno: {nota2:.1f}
c) Média do aluno  : {media:.1f}
d) Conceito        : D

O aluno foi REPROVADO!
        '''
        return resumo
    
    else:
        resumo = f'''------------SITUAÇÃO DO ALUNO------------
a) 1° nota do aluno: {nota1:.1f}
b) 2° nota do aluno: {nota2:.1f}
c) Média do aluno  : {media:.1f}
d) Conceito        : E

O aluno foi REPROVADO!
        '''
        return resumo


main()