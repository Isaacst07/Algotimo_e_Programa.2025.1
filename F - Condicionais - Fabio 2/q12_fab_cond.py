def main():
  numero = obter_numero_inteiro('Digite um número inteiro: ')

  eh_par_ou_impar(numero)


def eh_par_ou_impar(numero):
  if numero % 2 == 0:
    return print(f'O número {numero} é PAR!')
  else:
    return print(f'O número {numero} é ÍMPAR!')


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()