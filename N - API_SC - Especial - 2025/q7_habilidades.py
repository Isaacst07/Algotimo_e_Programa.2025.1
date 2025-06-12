# comecei 10:38
# terminei 10:58
# Domingo

from q1_number_utils import obter_numero_inteiro
from q1_number_utils import limpar_tela


def main():
    qtd_alunos_entrevistados = obter_numero_inteiro('Quantos alunos foram entrevistados: ')

    limpar_tela()

    total_alunos = 0 
    total_backend = 0
    total_frontend = 0 
    total_mobile = 0 
    total_dados = 0 
    contador = 1

    while contador <= qtd_alunos_entrevistados:
        habilidade = input('Habilidade do aluno(B = Backeend, F = Frontend, M = Mobile, D = Dados): ')
        n = int(habilidade.split() [0])
        tipo = habilidade.split()[1]
        total_alunos += n

        if tipo.upper() == 'B':
            total_backend += n
            
        if tipo.upper() == 'F':
            total_frontend += n

        if tipo.upper() == 'M':
            total_mobile += n

        if tipo.upper() == 'D':
            total_dados += n


        contador += 1

    limpar_tela()

    print(f'''------------RELATÓRIO DA PESQUISA------------
1) Total de alunos: {total_alunos} alunos
2) Total de Backend: {total_backend} 
3) Total de Frontend: {total_frontend} 
4) Total de Mobile: {total_mobile} 
5) Total de Dados: {total_dados} 
2) Percentual de Backend: {((total_backend / total_alunos) * 100):.2f}%
3) Percentual de Frontend: {((total_frontend / total_alunos) * 100):.2f}% 
4) Percentual de Mobile: {((total_mobile / total_alunos) * 100):.2f}%
5) Percentual de Dados: {((total_dados / total_alunos) * 100):.2f}%

''')
    

main()