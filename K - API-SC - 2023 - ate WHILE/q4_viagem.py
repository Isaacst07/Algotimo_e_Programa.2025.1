# [q4_viagem] José está planejando uma viagem com sua família
# para a Capital Federal. Para isso tem juntado Milhas em
# programas de fidelidade, e também pesquisando passagens
# aéreas diretamente. No Programa Smiles é possível comprar
# Milhas Aéreas pagando 70 reais a cada 1000 unidades. Uma
# passagem Teresina(THE) para Brasília(BSB) custa em torno de
# 21200 milhas, o mesmo voo(horário) tá por R$ 431. Ou seja,
# nesse caso, é melhor comprar em R$ que comprar Milhas a R$
# 70/Milheiro para então emitir o Voo.
# Entretanto no mundo das milhas, nunca compramos milhas a esse
# valor de 70 reais por mil, o que se faz é acumular milhas por meio
# de Cartão de Crédito e Compras Bonificadas. Neste caso,
# precifica-se as Milhas (valor convencionado) como baratas a R$
# 14,50 o Milheiro. Assim, o voo exemplificado acima as 21200
# Milhas custariam em reais o total de R$ 307,40. Desta forma,
# sendo vantajoso, ou seja, custa apena 71,3% do valor em R$
# normal (R$ 431)
# Faça um programa para auxiliar José no comparativo dos valor
# das passagens com Milhas Padrão(R$ 70), Milhas Acumuladas
# Baratas (R$ 14,50) e em Reais Normal (valor do site). Peça ao
# usuário Origem, Destino, Valor em R$ no site e Valor em Milhas no
# Site. Apresente para ele o valor equivalente em R$ caso compre
# com Milhas Padrão, indicando o % em relação ao valor em R$.
# Faça o mesmo para Milhas Baratas. Ao final, indique para ele a
# melhor forma de compra dentre as 3 opções.

import funcoes


def main():
    print('Olá, está querendo viajar?')
    funcoes.delay(750)
    print('Vou lhe ajudar nessa tarefa, com a opção que melhor caiba no seu bolso')
    funcoes.delay(750)
    print('Mas primeiro me responda algumas coisas, por favor!')
    print('')
    origem = funcoes.obter_str('Local de embarque(cidade): ')
    destino = funcoes.obter_str('Qual seu destino: ')
    milhas = funcoes.obter_numero_inteiro('Quantidade de Milhas da viagem: ')
    valor_site = funcoes.obter_numero_real('Valor da passagem no site(R$): ')
    milhas_areas = funcoes.obter_numero_real('Valor do milheiro no site(R$): ')
    milhas_padrao = (milhas / 1000) * milhas_areas
    milhas_baratas = (milhas / 1000) * 14.50

    funcoes.limpar_tela()

    print(f'''---------QUAL A MELHOR OPÇÃO?---------
Você que ir de {origem} para {destino}, dando um total de {milhas} milhas.

a) O valor da passagem no site é: R$ {valor_site:.2f}
b) O valor da passagem em Milhas Aréas é: R$ {milhas_padrao:.2f}
c) O valor da passagem em Milhas baratas é: R$ {milhas_baratas:.2f}

Ou seja, {calcular_melhor_compra(valor_site, milhas_padrao, milhas_baratas)}

''')
    

def calcular_melhor_compra(valor_site: float, milhas_padrao: float, milhas_baratas: float):
    
    if valor_site < milhas_baratas and valor_site < milhas_padrao:
        return 'É mais vantajoso comprar a passagem pelo site.'
    elif milhas_padrao < valor_site and milhas_padrao < milhas_baratas:
        return f'É mais vantajoso comprar a passagem pelas milhas do site, pois é {((milhas_padrao / valor_site) * 100):.1f}% do valor do site.'
    elif milhas_baratas < valor_site and milhas_baratas < milhas_padrao:
        return f'É mais vantajoso comprar a passagem pelas milhas baratas, pois é {((milhas_baratas / valor_site) * 100):.1f}% do valor do site.'


main()