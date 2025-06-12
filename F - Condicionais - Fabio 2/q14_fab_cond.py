def main():
    numero_1 = obter_numero_inteiro('Digite o primeiro número:')
    numero_2 = obter_numero_inteiro('Digite o segundo número:')
    numero_3 = obter_numero_inteiro('Digite o terceiro número:')
    numero_4 = obter_numero_inteiro('Digite o quarto número:')
    numero_5 = obter_numero_inteiro('Digite o quinto número:')

    media = calcular_media(numero_1, numero_2, numero_3, numero_4, numero_5)
    
    print(eh_maior(numero_1, media))
    print(eh_maior(numero_2, media))
    print(eh_maior(numero_3, media))
    print(eh_maior(numero_4, media))
    print(eh_maior(numero_5, media))

def calcular_media(numero_1, numero_2, numero_3, numero_4, numero_5):
   return (numero_1 + numero_2 + numero_3 + numero_4 + numero_5) / 5


def eh_maior(numero, media):
  if numero > media:
     return f'O número {numero} É MAIOR que a média {media} ! '
  else:
     return f'O número {numero} NÃO É MAIOR que a média {media}! '


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()