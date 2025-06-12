#comecei 23:12
# termienei 23:33
# Sábado

from q1_number_utils import obter_numero_inteiro_entre_faixa

def main():
    dia_data_1 = obter_numero_inteiro_entre_faixa('Digite o dia da 1° data: ', 1, 30)
    mes_data_1 = obter_numero_inteiro_entre_faixa('Digite o mês da 1° data: ', 1, 12)
    ano_data_1 = obter_numero_inteiro_entre_faixa('Digite o ano da 1° data: ', 1, 3000)
    dia_data_2 = obter_numero_inteiro_entre_faixa('Digite o dia da 2° data: ', 1, 30)
    mes_data_2 = obter_numero_inteiro_entre_faixa('Digite o mês da 2° data: ', 1, 12)
    ano_data_2 = obter_numero_inteiro_entre_faixa('Digite o ano da 2° data: ', 1, 3000)

    calcular_distacia(dia_data_1, mes_data_1, ano_data_1, dia_data_2, mes_data_2, ano_data_2)



def calcular_distacia(dia_1: int, mes_1: int, ano_1:int, dia_2: int, mes_2: int, ano_2: int):
    anos = diferenca_maior(ano_1, ano_2)
    meses = diferenca_maior(mes_1, mes_2)
    dias = diferenca_maior(dia_1, dia_2)

    if anos != 0 and meses != 0 and dias != 0:
        return print(f'A diferença das datas são: {anos} anos, {meses} meses e {dias} dias.')
    elif anos == 0 and meses != 0 and dias != 0:
        return print(f'A diferença das datas são: {meses} meses e {dias} dias.')
    elif anos == 0 and meses == 0 and dias != 0:
        return print(f'A diferença das datas são: {dias} dias.')
    elif anos != 0 and meses == 0 and dias == 0:
        return print(f'A diferença das datas são: {anos} anos.')
    elif anos == 0 and meses != 0 and dias == 0:
        return print(f'A diferença das datas são: {meses} meses.')
    elif anos != 0 and meses != 0 and dias == 0:
        return print(f'A diferença das datas são: {anos} anos e {meses} meses.')
    else:
        return print(f'As datas são iguais!')
   

def diferenca_maior(num1: int, num2: int):
    if num1 > num2:
        return num1 - num2
    elif num2 > num1:
        return num2 - num1
    else:
        return 0


main()