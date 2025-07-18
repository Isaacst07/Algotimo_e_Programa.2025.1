def main():
  qtd = int(input())

  for i in range(0, qtd, 1):
    numero = int(input())

    if eh_primo(numero):
      print('Prime')
    else:
      print('Not Prime')


def eh_primo(numero: int):
  if numero == 1:  
    return False

  candidato = 2

  while candidato < 500 and candidato < numero:
    if numero % candidato == 0:
      return False
    candidato += 1

  return True


main()