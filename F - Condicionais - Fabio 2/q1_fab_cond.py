def main():
    numero_1 = obter_numero_inteiro('Digite o primeiro número:')
    numero_2 = obter_numero_inteiro('Digite o segundo número:')
    numero_3 = obter_numero_inteiro('Digite o terceiro número:')

    Quantos_numeros_iguais = eh_igual(numero_1, numero_2, numero_3)

    print(f'{Quantos_numeros_iguais}')


def eh_igual(numero_1, numero_2, numero_3):
    if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 != numero_3:
       return 'Não tem números iguais!'
    elif numero_1 == numero_2 and numero_2 == numero_3:
        return 'Todos os números são iguais!'
    else: 
        return 'Só dois números são iguais!'


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()