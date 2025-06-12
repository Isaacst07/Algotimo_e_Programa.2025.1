import utils 


def main():
    utils.limpar_tela()

    litros_vendidos = utils.obter_numero_real('Quantidade de litros do combustível(L): ')
    tipo = utils.obter_string('Tipo do combustível(G - Gasolina ou A - Álcool): ')

    utils.limpar_tela()

    if tipo.upper() == 'G':
        print(calcular_gasolina(litros_vendidos))

    else:
        print(calcular_alcool(litros_vendidos))


def calcular_gasolina(litros_vendidos: float):
    valor_total = litros_vendidos * 2.5

    if litros_vendidos <= 20:
        desconto = valor_total * 0.04
        valor_final = valor_total - desconto
        return f'''Você colocou {litros_vendidos} litros de Gasolina, então:
a) Valor total do abastecimento: R$ {valor_total:.2f}
b) O desconto foi de: R$ {desconto:.2f}
c) Ápos o desconto o total a ser pago será: R$ {valor_final:.2f}

'''
    else: 
        desconto = valor_total * 0.06
        valor_final = valor_total - desconto
        return f'''Você colocou {litros_vendidos} litros de Gasolina, então:
a) Valor total do abastecimento: R$ {valor_total:.2f}
b) O desconto foi de: R$ {desconto:.2f}
c) Ápos o desconto o total a ser pago será: R$ {valor_final:.2f}

'''
    

def calcular_alcool(litros_vendidos: float):
    valor_total = litros_vendidos * 1.9

    if litros_vendidos <= 20:
        desconto = valor_total * 0.03
        valor_final = valor_total - desconto
        return f'''Você colocou {litros_vendidos} litros de Álcool, então:
a) Valor total do abastecimento: R$ {valor_total:.2f}
b) O desconto foi de: R$ {desconto:.2f}
c) Ápos o desconto o total a ser pago será: R$ {valor_final:.2f}

'''
    else: 
        desconto = valor_total * 0.05
        valor_final = valor_total - desconto
        return f'''Você colocou {litros_vendidos} litros de Álcool, então:
a) Valor total do abastecimento: R$ {valor_total:.2f}
b) O desconto foi de: R$ {desconto:.2f}
c) Ápos o desconto o total a ser pago será: R$ {valor_final:.2f}

'''


main()