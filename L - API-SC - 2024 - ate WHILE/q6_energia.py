# [energia.js] Em 2021 o Brasil voltou a enfrentar crise na matriz energética devido ao baixo nível das águas nos reservatórios das hidrelétricas
# brasileiras. Devido a isso os consumidores deverão arcar com custos extras (bandeira) para bancar outras matrizes energéticas, como usinas
# termoelétricas. Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de
# consumo será acrescido uma taxa extra de R$ 8,00.
# O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas.
# Valores hipotéticos:

# ● Consumo de até 30KWh isento de tarifa.
# ● Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
# ● acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos.

# Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS.
# A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80 KWh por mês, e custa 6% do valor tarifado (antes do
# impostos).
# Considerando os dados acima construa um software que receba dois dados:
# Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima.
# Como saída apresente os dados que compõem assim como o valor total a ser pago.
# Exemplo:
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00

import utils


def main():
    leitura_anterior = utils.obter_numero_inteiro('Leitura anterior(kwh): ')
    leitura_atual = utils.obter_numero_min('Leitura atual(kwh): ', leitura_anterior + 1 )
    utils.limpar_tela()

    calcular_talao(leitura_anterior, leitura_atual)


def calcular_talao(leitura_anterior: int, leitura_atual: int):
    consumo = leitura_atual - leitura_anterior
    icms = calcular_valor_consumo(consumo) * 0.25
    pis =  calcular_valor_consumo(consumo) * 0.15

    print(f'''-------------TALÃO DE ENERGIA-------------
a)Consumo: {consumo} KWh
b)Valor Faturado: R$ {(calcular_valor_consumo(consumo)):.2f}
c) Bandeira: R$ {((consumo // 100) * 8):.2f} ({consumo // 100} bandeiras)
d) ICMS: R$ {icms:.2f}
e) PIS/CONFIS: {pis:.2f}
f) Taxa Iluminação: R$ {calcular_taxa_iluminacao(consumo):.2f}

''')


def calcular_taxa_iluminacao(consumo: int ):
    
    if consumo >= 80:
        return calcular_valor_consumo(consumo) * 0.06
    else:
        return 0
    

def calcular_valor_consumo(consumo: int):

    if consumo <= 30:
        return 0
    elif consumo <= 100:
        return consumo * 0.59
    else:
        return consumo * 0.75


main()