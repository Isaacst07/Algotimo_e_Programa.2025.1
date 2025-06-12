def main():
  numero = obter_numero_inteiro('Digite um número: ')
  verificador_numero = eh_primo(numero)

  print(f'O número {numero} {verificador_numero} . ')


def eh_primo(numero = int):
  if numero == 2 or numero == 3 or numero == 5 or numero == 7 :
    return 'O número é PRIMO!'
  elif numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
    return 'O número é PRIMO!'
  else:
    return'O número não é PRIMO!'


def obter_numero_inteiro(label:str):
  return int(input(label))


main()