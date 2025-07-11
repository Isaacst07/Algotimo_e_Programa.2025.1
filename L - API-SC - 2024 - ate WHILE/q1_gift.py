# <!-- [gift.js] Uma loja presenteia suas clientes com descontos
# (cashback) progressivos de acordo com suas compras. Desta
# forma, para compras mensais de até R$ 250 reais, é feita a
# conversão (geração) de cashback de 5%; Para compras acima de
# R$ 250 até R$ 500, 7% de cashback; De R$ 500 até R$ 750, 8%
# de cashback; E para compras acima de R$ 750 é aplicado
# primeiramente as regras anteriores até R$ 750 do valor em cada
# faixa, e 25% sobre o valor acima de R$ 750. Operações de
# cashbacks progressivos têm o objetivo de incentivar as suas
# clientes a comprarem mais e ao mesmo tempo serem
# compensadas por isso.
# a. Implemente um software para auxiliar no cálculo do
# cashback mensal de suas clientes (devem ser lidos N
# compras Nome Cliente e Valor Compras).
# b. Informe quanto foi o faturamento total (soma das vendas);
# Quanto foi distribuído em cashback; Qual o valor em reais e
# percentual investido em cashback pela loja; Maior, menor e
# valor médio pago em cashback. -->

import utils


def main():
    cliente = utils.obter_nome('Nome do cliente: ')
    compras = utils.obter_numero_inteiro('Número de compras que o cliente realizou: ')

    contador = 0
    total_compras = 0 
    cashback_total = 0
    cashback_maior = None
    cashback_menor = None

    while contador < compras:
        valor_compras = utils.obter_numero_real('Valor da compra(R$): ')
        total_compras += valor_compras
        cashback_total += calcular_cashback(valor_compras)
        contador += 1

        if cashback_maior == None or calcular_cashback(valor_compras) > cashback_maior:
            cashback_maior = calcular_cashback(valor_compras)

        if cashback_menor == None or calcular_cashback(valor_compras) < cashback_menor:
            cashback_menor = calcular_cashback(valor_compras)

    print(f'''-------------RELATORIO DA COMPRA-------------
a) Cliente: {cliente}
b) Número de compras: {compras} compras
c) Faturamento total: {total_compras:.2f} R$
d) A loja distribuiu em cashback: {cashback_total:.2f} R$
e) Perncentual de cashback investido pela loja: {((cashback_total / total_compras) * 100):.2f}%
f) Maior valor de cashback: {cashback_maior:.2f} R$
g) Menor valor de cashback: {cashback_menor:.2f} R$
h) Valor médio de cashback: {calcular_media(cashback_total, compras):.2f}     
''')


def calcular_cashback (valor_compras: float):
   
        if valor_compras <= 250:
            return  valor_compras * 0.05
        elif valor_compras <= 500:
            return valor_compras * 0.07 
        elif valor_compras <= 750:
            return valor_compras * 0.08
        else:
            return  (250 * 0.05) + (500 * 0.07) + (750 * 0.08) + ((valor_compras - 750) * 0.25)
        

def calcular_media(soma: float, n: int):
    return soma / n
        

main()