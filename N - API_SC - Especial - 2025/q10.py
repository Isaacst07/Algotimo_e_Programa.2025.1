import q1_number_utils

def main():
    limite_min = q1_number_utils.obter_numero_inteiro('Informe o valor de A: ')
    limite_max = q1_number_utils.obter_numero_inteiro('Informe o valor de B: ', limite_max+11)

    controle = limite_min

    print(f'{controle}')