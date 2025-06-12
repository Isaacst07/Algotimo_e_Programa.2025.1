def main():
   angulo_1 = obter_numero_inteiro('Primeiro ângulo do triângulo: ')
   angulo_2 = obter_numero_inteiro('Segundo ângulo do triângulo: ')
   angulo_3 = obter_numero_inteiro('Terceiro ângulo do triângulo: ')

   print(forma_triangulo(angulo_1, angulo_2, angulo_3))


def forma_triangulo(angulo_1, angulo_2, angulo_3):
  if angulo_1 + angulo_2 + angulo_3 == 180:
    return (f'Formar um TRIÂNGULO e sua classificação {classificar_triangulo(angulo_1, angulo_2, angulo_3)}')
  else:
    return 'NÃO formar um triângulo,logo não tem classificação.'


def classificar_triangulo(angulo_1, angulo_2, angulo_3):
  if angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    return 'é RENTÂNGULO!'
  elif angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
    return 'é ÂCUTANGULO!'
  else: angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90
  return 'é OBTUSÂNGULO!'


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()