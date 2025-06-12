import utils 

def main():
    print('Promoção na frutaria do Isaac!')
    utils.dar_espaco()
    print('            Até 5 Kg        Acima de 5 Kg')
    print('Morango: R$ 2,50 por Kg|   R$ 2,20 por Kg|')
    print('Maçã:    R$ 1,80 por Kg|   R$ 1,50 por Kg|')

    utils.dar_espaco()

    tipo_fruta = utils.obter_string('Qual a fruta(Morango ou Maçã): ')
    quilos = utils.obter_numero_real('Quantos quilos(Kg): ')

    utils.limpar_tela()

    print(calcular_compra(tipo_fruta, quilos))


def calcular_compra(tipo_fruta: str, quilos: int):

    if tipo_fruta.upper() == 'MAÇÃ' or tipo_fruta.upper() == 'MAÇA'or tipo_fruta.upper() == 'MACA':
        print(f'Você comprou {quilos:.2f} Kg de Maçã, então:')
        if quilos <= 5:
            valor_total = quilos * 1.8
            return f'O valor total ser pago é R$ {valor_total:.2f}'

        else: 
            valor_total = quilos * 1.5
            if valor_total >= 25:
                valor_final = valor_total - (valor_total * 0.1)
                return f'O valor total a ser pago é R$ {valor_final:.2f}'
            else:
                return f' O valor total a ser é R$ {valor_total:.2f}'
            
    else:
        print(f'Você comprou {quilos:.2f} Kg de Morango, então:')
        if quilos <= 5:
            valor_total = quilos * 2.50
            return f'O valor total ser pago é R$ {valor_total:.2f}'

        else: 
            valor_total = quilos * 2.20
            if valor_total >= 25:
                valor_final = valor_total - (valor_total * 0.1)
                return f'O valor total a ser pago é R$ {valor_final:.2f}'
            else:
                return f' O valor total a ser é R$ {valor_total:.2f}'







main()