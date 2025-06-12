# (q3_covid.py) Durante a Pandemia da COVID, diariamente o
# noticiário informava à população dados importantes sobre a
# evolução e controle da doença. Neste cenário, usa-se atualmente
# o conceitos de “Em queda”, “Em Alta” e “Em Estabilidade”
# baseada nos números do dia. Variações menores que 15% nos
# números indicam "Em Estabilidade".
# Construa um programa que calcule e classifique a variação dos
# dados de acordo com o explicado. As entradas são vários
# números que representam a quantidade casos no dia. Os
# operadores podem, por erro, digitar valores inválidos com letras,
# números negativos, ou outros valores absurdos.
# Considerar apenas os inteiros não negativos. O programa deve
# parar quando for digitado exatamente “fim”. Após cada número
# mostrar o conceito do dia, ou “valor não computador” caso o valor
# seja inválido. E após o fim, mostrar total de casos, e média de
# casos por dia.

# Domingo 
# comecei 12:05
# terminei 12:45 

from q1_number_utils import obter_numero_inteiro
from q1_number_utils import limpar_tela


def main():
    casos_atuais = obter_numero_inteiro('Quantidade de casos até o momento: ')
    casos_totais = 0 
    qtd_dias = 0 

    while True:
        limpar_tela()

        casos_do_dia = input('Quantidades de casos do dia(fim == PARAR): ')
        print('')

        if casos_do_dia.lower() == 'fim':
            break

        if obter_casos_inteiro(casos_do_dia) == True:
            casos_do_dia = int(casos_do_dia)
            queda = casos_atuais * 0.85
            alta = casos_atuais * 1.15

            print(f'{situacao_do_dia(casos_do_dia, alta, queda)}')

            print('')

            input('Aperte <Enter> para continuar ...')

            casos_atuais = casos_do_dia
            casos_totais += casos_do_dia
        

        else:
            print(f'Valor não computado!')
            input('Aperte <Enter> para continuar ...')
        
        qtd_dias += 1

    limpar_tela()

    print(f'''----------RELATÓRIO----------
1) Total de casos: {casos_totais} casos
2) Média de casos por dia: {(casos_totais / qtd_dias):.2f} casos por dia

''')


def situacao_do_dia(casos: int, alta: int, queda: int):
    casos = int(casos)

    if casos >= alta:
        return 'Situação do dia: EM ALTA'
    elif casos <= queda:
        return 'Situaçaõ do dia: EM QUEDA'
    else:
        return 'Situaçaõ do dia: EM ESTABILIDADE'
    

def obter_casos_inteiro(entrada):
    try:
        numero = int(entrada) 
        if numero >= 0:
            return True
    except ValueError:
        return False
        
        
main()