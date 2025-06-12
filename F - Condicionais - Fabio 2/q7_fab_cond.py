def main():
   lado_1 = obter_numero_inteiro('Primeiro lado do triângulo: ')
   lado_2 = obter_numero_inteiro('Segundo lado do triângulo: ')
   lado_3 = obter_numero_inteiro('Terceiro lado do triângulo: ')

   print(forma_triangulo(lado_1, lado_2, lado_3))


def forma_triangulo(lado_1, lado_2, lado_3):
  if lado_1 + lado_2 >= lado_3 and lado_1 + lado_3 >= lado_2 and lado_2 + lado_3 >= lado_1:
    return (f'Formar um TRIÂNGULO e sua classificação {classificar_triangulo(lado_1, lado_2, lado_3)}')
  else:
    return 'NÃO formar um triângulo,logo não tem classificação.'


def classificar_triangulo(lado_1, lado_2, lado_3):
  if lado_1 == lado_2 and lado_2 == lado_3:
    return 'é EQUILÁTERO!'
  elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    return 'é ISÓSCELES!'
  else: lado_1 != lado_2 and lado_2 != lado_3
  return 'é ESCALENO!'


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()