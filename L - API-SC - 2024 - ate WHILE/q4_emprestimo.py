# [empréstimo.py] João precisa de um dinheiro emprestado para
# comprar um Notebook para estudar programação. Para isso, foi ao
# RSBank fazer uma simulação. As taxas de empréstimo do banco
# obedecem à regra dos Juros Compostos Mensais, ou seja, o valor é
# calculado cumulativamente mês a mês, ou seja, aplica-se os juros
# sobre o valor total no primeiro mês e esse passa a ser a base para o
# segundo mês.
# Porém a taxa de juros aplicada é calculada de acordo com o prazo
# de parcelamento (vide tabela) e à SELIC, atualmente em 13,75%
# (abril/2023). O usuário só pode parcelar o empréstimo em até 24x
# (min. 2 parcelas). Valor mínimo de empréstimo é de um salário
# mínimo. Valor máximo de parcela é 40% da Renda Mensal do
# Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre
# Operações Financeiras) pago ao Governo Federal antes de aplicar
# os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor
# total (independente do prazo) + 0,0082% por cada dia do prazo do
# empréstimo. Considere todos os meses com 30 dias. Os juros são
# aplicados sobre o valor a ser recebido pelo Cliente + IOF

# Prazo Taxa
# Até 6x 50% da SELIC
# de 7x a 12x 75% da SELIC
# de 12x a 18x 100% da SELIC
# Acima de 18x 130% da SELIC

# ● Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
# desejados, valide os dados a serem recebidos.

# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO (se a
# renda mensal suporta a parcela)
# selic 13.75%

#Valor máximo de parcela é 40% da Renda Mensal do
# Cliente.

import utils


def main():
    utils.limpar_tela()
    print('Óla,vamos simular o empréstimo para você!')
    print('')
    renda_mensal = utils.obter_numero_real('Dígite sua renda mensal(R$): ')
    valor_emprestimo = utils.obter_numero_min('Valor do empréstimo desejado(R$): ', 1518)
    prazo = utils.obter_numero_entre('Qual o prazo mensal desejado(mínimo 2x): ', 2, 24)
    utils.limpar_tela()

    calcular_emprestimo(renda_mensal, valor_emprestimo, prazo)



def calcular_emprestimo(renda_mensal: float, valor_emprestimo: float, prazo: int):
    iof = valor_emprestimo * (0.38 / 100) + (valor_emprestimo * ((0.0082 / 100) * (prazo * 30 )))

    (0.0082 / 100)
    if prazo <= 6:
        taxa_mensal = 0.1375 * 0.5
    elif prazo <= 12:
        taxa_mensal = 0.1375 * 0.75
    elif prazo <= 18:
        taxa_mensal = 0.1375 * 1
    else: 
        taxa_mensal = 0.1375 * 1.3

    valor_total_com_iof = valor_emprestimo + iof
    valor_total_final = valor_total_com_iof * ((1 + taxa_mensal) ** prazo)
    parcela_mensal = valor_total_final / prazo
    comprometimento_mensal = (parcela_mensal / renda_mensal) / 100
    status = 'APROVADO' if comprometimento_mensal <= 40 else 'NEGADO, a renda mensal não suporta a parcela'

    print(f'''-----------------SIMULAÇÃO EMPRÉSTIMO-----------------
a) Valor Pedido: R$ {valor_emprestimo:.2f} 
b) Valor do IOF: R$ {iof:.2f} 
c) Valor dos Juros a pagar: R$ {(valor_total_final - valor_total_com_iof):.2f} 
d) Valor Total a pagar: R$ {valor_total_final:.2f} 
e) Valor da Parcela Mensal: {prazo}x de  R$  {parcela_mensal:.2f}
f) Comprometimento da Renda Mensal (%): {comprometimento_mensal:.2f}%
g) Se Empréstimo APROVADO ou NEGADO: {status} 

''')


main()