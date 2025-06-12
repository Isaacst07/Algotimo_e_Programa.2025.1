def obter_numero_real(label: str):
  return float(input(label))


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

def obter_numero_interio_min(label:str, min ):
 numero = obter_numero_inteiro(label)
 min = 1000
 max = 9999
 if  min <= numero <= max:
    return numero
 else:
    print(f'O número deve ser no mínimo {min} e no máximo {max}')
    return print(obter_numero_interio_min(label))
  