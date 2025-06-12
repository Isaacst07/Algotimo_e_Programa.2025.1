# [investimento.js] Mariana resolveu investir de parte de seu salário
# (um pedaço(R$) inferior a 30%) de forma fixa mensal; O investimento
# escolhido rende mensalmente a uma taxa de juros de 0,01% até 1,00
# % sobre o saldo do mês. Mariana tem um dado objetivo com este
# investimento. Pergunte a ela qual o objetivo e de quanto ela precisa
# para realizá-lo. Além disso, peça o salário, quanto(%) ela pretende
# investir mensalmente e qual a taxa de juros do investimento
# escolhido. Em seguida mostre em quantos meses ela atingirá o
# objetivo. Se for acima de 12 meses mostre-o em anos e meses. A
# cada mês você deve atualizar o saldo primeiro com o aporte
# (depósito de valor do salário) e depois aplicar os créditos dos juros

# sobre esse novo saldo. Faça isso enquanto o objetivo não for
# alcançado, contando os meses para serem exibidos como se pede.

import utils


def main():
    salario = utils.obter_numero_real('Qual seu salário(R$): ')
    investimento = utils.obter_numero_entre('Quanto vai usar do seu salário mensalmente (até 30%): ', 0, 30)
    taxa_juros = utils.obter_numero_entre('Qual a taxa de juros do investimento(entre 0,01% e 1,00%): ', 0.01, 1.00 )
    objetivo = utils.obter_nome('Qual seu objetivo: ')
    realizar_obj = utils.obter_numero_real('Quanto precisa para relizar o objetivo(R$): ')

    utils.limpar_tela()

    calcular_investimento(salario, investimento, taxa_juros, objetivo, realizar_obj)


def calcular_investimento(salario: float, investimento: float, taxa_juros: float, objetivo: str, realizar_obj: float):
    investimento_mes = salario * (investimento / 100)
    total_acumulado = 0
    tempo = 0

    taxa_mensal = taxa_juros / 100

    while total_acumulado < realizar_obj:
        total_acumulado += investimento_mes  
        total_acumulado *= (1 + taxa_mensal)  
        tempo += 1

    print(f'''------------PARA REALIZAR {objetivo.upper()}------------
a) Para realizar seu objetivo era necessário: R$ {realizar_obj:.2f}
b) Você investiu mensalmente: R$ {investimento_mes:.2f}
c) Sob uma taxa de juros de: {taxa_juros:.2f}% ao mês
d) Sob essas condições, você levará: {calcular_tempo(tempo)}

''')


def calcular_tempo(tempo: int):
    if tempo > 12:
        anos = tempo // 12
        meses = tempo % 12
        return f'{anos} anos e {meses} meses'
    else:
        return f'{tempo} meses'


main()