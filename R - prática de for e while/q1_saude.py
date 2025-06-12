import os


def main():
    print('Olá, vamos ajudar você a controlar seus consumos de calorias!')
    print('')

    periodo = obter_numero_int('Qual período de tempo você quer analisar: ')
    limite_cal = obter_numero_int('Limite de calorias para consumir no dia: ')
    total_cal_periodo = 0 
    maior_consumo = 0
    menor_consumo = 0 
    dia_menor_consumo = 0
    dia_maior_consumo = 0

    limpar_tela()

    for i in range (1, periodo + 1, 1):

        limpar_tela()

        print(f'-----------------DIA {i}-----------------')
        cafe_manha = obter_numero_int('Quantidade de calorias do café da manhã do dia: ')
        almoco = obter_numero_int('Quantidade de calorias do almoço do dia : ')
        janta = obter_numero_int('Quantidade de calorias da janta do dia: ')
        lanche = obter_numero_int('Quantidade de calorias dos lanches do dia: ')
        print('')

        consumo_total = cafe_manha + almoco + janta + lanche
        total_cal_periodo += consumo_total

        if consumo_total > limite_cal:
            print(f'Opa,seu consumo do dia foi de {consumo_total} cal, excedendo o limite diário de {limite_cal} cal.')
        else:
            print(f'Está tudo bem você não execedeu o limite diário,você consumiu {consumo_total} cal e o limite de calorias é {limite_cal} cal.')

        if maior_consumo == 0 or consumo_total > maior_consumo:
            maior_consumo = consumo_total
            dia_maior_consumo = i

        if menor_consumo == 0 or consumo_total < menor_consumo:
            menor_consumo = consumo_total
            dia_menor_consumo = i
            
        input('Enter to continue ...')
    
    media_periodo = total_cal_periodo  / periodo
     
    limpar_tela()

    resultado = f'''------------RESUMO DO PERÍODO------------
a) A média calórica do período: {media_periodo:.2f} cal
b) o dia com o menor consumo: {menor_consumo} cal no {dia_menor_consumo}° dia
c) o dia com o maior consumo: {maior_consumo} cal no {dia_maior_consumo}° dia
'''
    
    print(resultado)


def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{numero}" digitado não é um inteiro válido!')
        obter_numero_int(label)


def limpar_tela():
    os.system('cls')


main()