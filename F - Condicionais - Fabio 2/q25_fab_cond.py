def main():
    senha = obter_numero_interio_min('Dígite uma senha de 4 dígitos: ')
    
    validar_senha(senha)


def validar_senha(senha):
  if senha == 1234:
    return print('Senha correta,PARABÉNS!!!')
  else:
    print('Senha incorreta tente novamente :(')
    

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


def obter_numero_interio_min(label:str ):
  numero = obter_numero_inteiro(label)
  min = 1000
  max = 9999
  if  min <= numero <= max:
    return numero
  else:
    print(f'A senha deve ser de 4 dígitos ')
    return print(obter_numero_interio_min(label))


main()