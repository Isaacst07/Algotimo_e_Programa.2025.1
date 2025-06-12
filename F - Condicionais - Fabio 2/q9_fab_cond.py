def main():
  numero = obter_numero_interio_min('Digite um número entre 0 e 100: ')
  
  print(f'O número {numero} {eh_primo(numero)} . ')


def eh_primo(numero):
  if numero == 2 or numero == 3 or numero == 5 or numero == 7 :
    return 'É um número é PRIMO!'
  elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
    return 'É um número é PRIMO!'
  else:
    return'NÃO é um número primo!'
  
  
def obter_numero_interio_min(label:str ):
  numero = obter_numero_inteiro(label)
  min = 0
  max = 100
  if  min <= numero <= max:
    return numero
  else:
    print(f'O número deve ser no mínimo {min} e no máximo {max}')
    return print(obter_numero_interio_min(label))
  

def obter_numero_inteiro(label:str):
  return int(input(label))


main()