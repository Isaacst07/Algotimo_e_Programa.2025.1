def main():
  horas_comecou = obter_numero_inteiro('Horas que o jogo começou: ')
  minutos_comecou = obter_numero_inteiro('Minutos que começou o jogo: ')
  horas_terminou = obter_numero_inteiro('Horas que o jogo terminou: ')
  minutos_terminou = obter_numero_inteiro('Minutos que começou o terminou: ')
   
  calcular_horas(horas_comecou, horas_terminou, minutos_comecou, minutos_terminou)


def calcular_horas(horas_comecou, horas_terminou, minutos_comecou, minutos_terminou):
  calcular_horas = horas_terminou - horas_comecou
  calcular_minutos = minutos_terminou - minutos_comecou
  return print(f'O jogo começou {horas_comecou}h{minutos_comecou}min e terminou {horas_terminou}h{minutos_terminou}min,então o jogo durou {calcular_horas}h{calcular_minutos}min . ')

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()