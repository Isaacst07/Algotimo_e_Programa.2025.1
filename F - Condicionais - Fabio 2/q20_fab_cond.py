def main():
  angulo = obter_numero_interio_min('Digite o ângulo: ')

  qual_quadrante_do_angulo(angulo)


def qual_quadrante_do_angulo(angulo):
  if angulo <= 90:
    return print('Este ângulo está no PRIMEIRO QUADRANTE!')
  elif angulo <= 180:
    return print('Este ângulo está no SEGUNDO QUADRANTE!')
  elif angulo <= 270:
    return print('Este ângulo está no TERCEIRO QUADRANTE!')
  else: angulo <= 360
  return print('Este ângulo está no QUARTO QUADRANTE')


def obter_numero_interio_min(label:str ):
  numero = obter_numero_inteiro(label)
  min = 0
  max = 360
  if  min <= numero <= max:
    return numero
  else:
    print(f'A opção escolhida deve ser entre o ângulo mínimo 0° e o ângulo máximo 360°')
    return print(obter_numero_interio_min(label))
  

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()