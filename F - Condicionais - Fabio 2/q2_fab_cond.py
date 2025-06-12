def main():
    numero_1 = obter_numero_inteiro('Digite o primeiro número: ')
    numero_2 = obter_numero_inteiro('Digite o segundo número: ')

    print (eh_maior(numero_1, numero_2))


def eh_maior(numero_1, numero_2):
    if numero_1 > numero_2:
        return (f'{numero_1} é o MAIOR entre os números e {numero_2} é o MENOR entre os números.')
    elif numero_2 > numero_1:
        return (f'{numero_2} é o MAIOR entre os números e {numero_1} é o MENOR entre os números.')
    else:
        return (f'Os números {numero_1} e {numero_2} são iguais!')
    

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()