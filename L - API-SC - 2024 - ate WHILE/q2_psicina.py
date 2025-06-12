# [piscina.js] Uma piscina é algo muito legal de ter (...um amigo que
# tenha uma). Para evitar transbordar ao tomar banho na piscina é
# bom deixar o nível da água com no máximo 85% da capacidade.
# Assim uma piscina que comporta 20 mil litros de água é bom botar
# só 17 mil litros. Considere uma piscina estilo quadrada. Para
# encher a piscina ele usará água paga (o valor é cobrado por cada
# 1000 litros de água, em partes inteiras. Ou seja, se usar 1 litro já
# paga por 1000, ao usar 1002 já paga 2 mil litros)
# a. Calcule a capacidade máxima da piscina pedindo ao usuário as
# dimensões de largura, comprimento e profundidade (em cm). 1 litro é
# igual a 1000 cm3

# . Uma piscina por exemplo de capacidade →
# L=100cm x C=100cm x P=100cm → 1000 litros, e deve ser cheia até
# 850 litros apenas.
# b. Informe até quantos litros é recomendado encher a piscina.
# c. Peça ao usuário para informar o valor a ser pago por cada 1000 litros
# na concessionária de água de sua cidade, e informe quanto ele
# gastará para encher sua piscina;
# d. Mensalmente é necessário repor 10% da água devido a banho e
# evaporação, informe ao usuário também o gasto mensal para manter
# a piscina no nível ideal.

import utils 

def main():
    largura = utils.obter_numero_real('Largura da psicina em cm: ')
    comprimento = utils.obter_numero_real('Comprimento da psicina em cm: ')
    profundidade = utils.obter_numero_real('Profundidade da psicina em cm: ')
    valor_1000l = utils.obter_numero_real('Valor de 1000 litros na sua cidade (R$): ')
    
    utils.limpar_tela()
    
    capacidade_psicina(largura, comprimento, profundidade, valor_1000l)


def capacidade_psicina(largura: float, comprimento: float, profundidade: float, valor_1000l: float):
    capacidade_total = (largura * comprimento * profundidade) / 1000
    capacidade_ideal = capacidade_total * 0.85 
    repor_mensal = capacidade_ideal * 0.1
    gasto_mensal = repor_mensal * valor_1000l


    print(f'''
a)Capacidade total da sua psicina: {capacidade_total:.0f} L
b)Recomendace encher 85% da pscina no seu caso: {capacidade_ideal:.0f} L
c)Para encher a pscina você gastará: {encher_psicina(capacidade_ideal, valor_1000l):.2f} R$
d)A cada mês é bom repor 10% : {repor_mensal:.0f} L,ou seja, {gasto_mensal:.2f} R$
''')
    

def encher_psicina(capacidade_ideal: float, valor_1000l: float):

    if (capacidade_ideal % 1000) != 0:
        return ((capacidade_ideal // 1000) * valor_1000l) + valor_1000l
    elif (capacidade_ideal % 1000) == 0:
        return (capacidade_ideal / 1000) * valor_1000l
    else: (capacidade_ideal % 1000) > 0
    return valor_1000l


main()