def main():
  numero = obter_numero_interio_min('Digite um número inteiro de 2 dígitos: ')
  algorismo_dezena = calcular_algorimos_dezena(numero)
  algarismo_unidade = calcular_algarismo_unidade(numero)
  
  print(eh_igual(algorismo_dezena, algarismo_unidade))


def calcular_algorimos_dezena(numero):
  return numero // 10


def calcular_algarismo_unidade(numero):
  return  numero % 10


def eh_igual(algorismo_dezena, algorismo_unidade):
  if algorismo_dezena == algorismo_unidade:
    return (f'Os algorismos de dezena e unidade são iguais, sendo eles {algorismo_dezena}. ')
  else:
    return (f'O algorimo da dezena é {algorismo_dezena} e o algorismo da unidade é {algorismo_unidade},portanto são diferente. ')


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

def obter_numero_interio_min(label:str):
  valor = obter_numero_inteiro(label)
  min = 10
  max = 99

  if valor >= min and valor <= max:
    return valor
  else:
    print(f'O número deve ser maior que o mínimo({min}) e menor que o máximo({max}), já que é um número de dois digítos.)')
  return obter_numero_interio_min(label)


main()