def main():
  nota_1 = float(input('Nota 1: '))
  nota_2 = float(input('Nota 2: '))
  nota_3 = float(input('Nota 3: '))

  media = calcular_media(nota_1, nota_2, nota_3)

  print(f'Com as suas notas {nota_1:.1f}, {nota_2:.1f} e {nota_3:.1f} sua média foi {media:0.1f} .')
  
  if nota_1 == 0.0 or nota_2 == 0.0 or nota_3 == 0.0 or media < 5:
    print('Então você está REPROVADO!')
  elif media < 7.0:
    print('Então você está de RECUPERAÇÃO!')
  else: 
    print('Então você está APROVADO!')

  

def calcular_media(nota_1, nota_2, nota_3):
  return (nota_1 + nota_2 + nota_3) / 3


def obter_numero_real(label: str):
  return float(input(label))


main()