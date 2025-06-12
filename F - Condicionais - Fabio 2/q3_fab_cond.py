def main():
    numero_1 = obter_numero_inteiro('Digite o primeiro número: ')
    numero_2 = obter_numero_inteiro('Digite o segundo número: ')
    numero_3 = obter_numero_inteiro('Digite o terceiro número: ')

    print(eh_maior(numero_1, numero_2, numero_3))


def eh_maior(numero_1, numero_2, numero_3):
    if numero_1 == numero_2 and numero_1 > numero_3:
        return (f'{numero_1} é o MAIOR entre os números. ')
    elif numero_1 == numero_2 and numero_1 < numero_3:
        return (f'{numero_3} é o MAIOR entre os números. ')
    elif numero_1 > numero_2 and numero_1 > numero_3:
        return (f'{numero_1} é o MAIOR entre os números! ')
    elif numero_2 > numero_1 and numero_2 > numero_3:
        return (f'{numero_2} é o MAIOR entre os números! ')
    elif numero_3 > numero_1 and numero_3 > numero_2:
        return (f'{numero_2} é o MAIOR entre os números! ')
    else:
        return (f'Os números são IGUAIS!')
    

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()