# Faça um programa para auxílio o Prof. Joaquim ter
# dados sobre rendimento numa avaliação que aplicou a seus
# aluno. O professor irá digitar as notas de seus alunos e você deve
# computar: Maior Nota Geral, Menor Nota Geral, Média Geral da
# turma,. Performance das Notas dos Homens(escala 0 a 100%),
# Performance das Mulheres (escala 0 a 100%). A entrada será
# Sexo (M ou F) e Nota (número entre 1 e 10). Encerra quando sexo
# for diferente de M e F. Mostre quanto alunos, quantos de cada
# sexo, também. Classifique o desempenho da turma, e também
# homens e mulheres, em:

#a. Péssimo [0 a 2]
#b. Ruim ]2 a 4]
#c. Regular [4 a 7[
#d. Bom [7 a 8[
#e. Excelente [8 a 10]


import funcoes


def main():
    total_alunos = 0
    maior_nota = 0
    menor_nota = 0
    soma_notas = 0
    masc = 0
    fem = 0
    nota_fem = 0
    nota_masc = 0


    while True:
     sexo = str(input('Qual o sexo do aluno(M - MASCULINO ou F - FEMININO): '))

     if sexo != 'M' and sexo != 'F' :
        break
     
     nota = funcoes.obter_numero_entre('Digite a sua nota: ', 1, 10)

     funcoes.limpar_tela()

     if sexo == 'M':
        masc += 1
        nota_masc += nota
     if sexo == 'F':
        fem += 1
        nota_fem += nota
    
     if nota > maior_nota:
        maior_nota = nota
     if menor_nota == 0 or nota < menor_nota:
        menor_nota = nota
     total_alunos += 1
     soma_notas += nota

    
    media_turma = soma_notas/(fem+masc)
    media_fem = nota_fem/fem
    media_masc = nota_masc/masc

    funcoes.limpar_tela()

    print(f'''--------------SITUAÇÃO DA TURMA--------------
a) Total de alunos: {masc + fem} alunos
b) Total de alunos M: {masc} alunos masculinos
c) Total de alunos F: {fem} alunas femininas
d) Maior nota geral: {maior_nota}
e) Menor nota geral: {menor_nota}
f) Média geral da turma: {media_turma}
g) Desempenho da turma: {desempenho(media_turma)}
h) Média Masculina: {media_masc}
i) Desempenho Masculino: {desempenho(media_masc)}
j) Média Feminina: {media_fem}
k) Desempenho Feminino: {desempenho(media_fem)}
l) Performacer dos homens(%): {((nota_masc / soma_notas) * 100):.2f}%
m) Performacer das mulheres(%): {((nota_fem / soma_notas) * 100):.2f}%
 ''')
 
   
def desempenho(media: float):
    if media <= 2:
        return 'Desempenho PÉSSIMO'
    elif media <= 4:
        return 'Desempenho RUIM'
    elif media < 7 :
        return 'Desempenho REGULAR'
    elif media < 8:
        return 'Desempenho BOM'
    elif media <= 10:
        return 'Desempenho EXECELENTE'

      
main()