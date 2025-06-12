# [serasa.js] A SERASA começou a implantar o Serasa Score 2.0 em 2021. O Score é uma forma de avaliar o perfil do consumidor no momento da
# aquisição de crédito, seja cartão de crédito ou financiamento de um veículo, apartamento ou empréstimo pessoal. Desta forma são avaliadas algumas
# entradas de dados históricos consumidor e, caso não esteja negativado, apresentando um valor entre 0 e 1000.
# Baseado nisso, faça um programa que receba valores de 0 a 100 em cada um dos 3 critérios de cálculo, ou seja, como se fosse uma Escala, no item
# a. você pode ter de 0 a 100, se for 100, por exemplo, significa 100% dos pontos previstos, assim Score 1.0 (260) e Score 2.0 (620), se fosse 50%
# então esse item a. seria 130 e 310, respectivamente em cada Score 1.0 e 2.0. Aplique essa formula de cada uma e apresente o valor do Score tanto
# versão Score 1.0 quanto na versão Score 2.0.

# Critérios de cálculo

# Serasa
# Score
# 1.0
# Serasa
# Score 2.0

# a. Dados positivos (cartão de
# crédito, consórcio, consignado,
# empréstimos e financiamentos)
# comportamentos de pagamento,
# tempo dos contratos e tipos de
# contratos

# 26%
# (260)
# 62%
# (620)

# b. Informações de dívidas, histórico
 #de regularização e em aberto

# 57%
# (570)
# 19%
# (190)

# c. Consultas para novos contratos
# de serviço ou crédito

# 17%
# (170)
# 19%
# (190)

# Com os dois Scores (1.0 e 2.0) calculados, classifique o Perfil do
# Cliente acordo com a tabela abaixo e apresente a ele o resultados:
# Classificação de risco de tomador de crédito
# Faixa de score Score antigo Score novo
# Muito bom 800-1000 701-1000
# Bom 600-800 501-700
# Regular 400-600 301-500
# Baixo 0-400 0-300
# Fonte: Serasa
# Exemplo entrada:
# a: 70
# b: 55
# c: 100
# Saída:
# Score 1.0: valor - categoria
# Score 2.0: valor - categoria
import utils 


def main():
    utils.limpar_tela()
    print('Óla, vamos ver como estar seu score?')

    a = utils.obter_numero_entre('a (Dados positivos): ', 0, 100)
    b = utils.obter_numero_entre('b (Informações de dívidas, histórico de regularização e em aberto): ', 0, 100)
    c = utils.obter_numero_entre('c (Consultas para novos contratos de serviço ou crédito): ', 0, 100)
    utils.limpar_tela()

    calcular_score_1(a , b, c)
    calcular_score_2(a , b, c)


def calcular_score_1(a: int, b: int, c: int):
    score = ((a / 100) * 260) + ((b / 100) * 260) + ((c / 100) * 260)

    if score <= 400:
        print(f'Score 1.0: {score} - Baixo')
    elif score <= 600:
        print(f'Score 1.0: {score} - Regular')
    elif score <= 800:
        print(f'Score 1.0: {score} - Bom')
    elif score <= 1000:
        print(f'Score 1.0: {score} - Muito bom')
    else:
        print(f'Score 1.0: {score} - Mais do que bom')


def calcular_score_2(a: int, b: int, c: int):
    score = ((a / 100) * 620) + ((b / 100) * 620) + ((c / 100) * 620)

    if score <= 300:
        print(f'Score 2.0: {score} - Baixo')
    elif score <= 500:
        print(f'Score 2.0: {score} - Regular')
    elif score <= 700:
        print(f'Score 2.0: {score} - Bom')
    elif score <= 1000:
        print(f'Score 2.0: {score} - Muito bom')
    else:
        print(f'Score 2.0: {score} - Mais do que bom')


main()