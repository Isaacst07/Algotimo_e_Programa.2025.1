def main():
  nota_1 = obter_numero_real('Nota 1: ')
  nota_2 = obter_numero_real('Nota 2: ')

  media = calcular_media(nota_1, nota_2)

  print(f'Com as suas notas {nota_1:.1f}, {nota_2:.1f}  sua média foi {media:0.1f} .')
  
  if media >= 7:
    print('Então você está APROVADO!') 
  else: 
    return print(exame_final(media))
    

def exame_final(media):
  nota_exame_final = obter_numero_real('Nota exame final: ')
  if calcular_media(media, nota_exame_final) >= 5:
    return f'Você está APROVADO'
  else: calcular_media(media, nota_exame_final) < 5
  return 'você está REPROVADO'


def calcular_media(nota_1, nota_2):
  return (nota_1 + nota_2 ) / 2


def obter_numero_real(label: str):
  return float(input(label))


main()