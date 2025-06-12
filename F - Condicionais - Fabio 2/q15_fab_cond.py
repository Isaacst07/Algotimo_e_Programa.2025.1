def main():
  horas_prof_1 = obter_numero_real('Quantas horas o primeiro professor trabalhou(h): ')
  valor_horas_prof_1 = obter_numero_real('Quanto recebe por horas o primeiro professor(R$): ')
  horas_prof_2 = obter_numero_real('Quantas horas o segundo professor trabalhou(h): ')
  valor_horas_prof_2 = obter_numero_real('Quanto recebe por horas o segundo professor(R$): ')

  ganho_total_prof_1 = total_ganho(horas_prof_1, valor_horas_prof_1)
  ganho_total_prof_2 = total_ganho(horas_prof_2, valor_horas_prof_2)

  print(eh_maior(ganho_total_prof_1, ganho_total_prof_2))


def total_ganho(horas, valor_por_hora):
  return horas * valor_por_hora


def eh_maior(ganho_total_prof_1, ganho_total_prof_2):
  if ganho_total_prof_1 > ganho_total_prof_2:
    return f'O professor 1 é o que ganha mais, ganhando {ganho_total_prof_1:.2f}R$,enquanto o professor 2 ganha {ganho_total_prof_2:.2f}R$ .'
  elif ganho_total_prof_2 > ganho_total_prof_1:
    return f'O professor 2 é o que ganha mais, ganhando {ganho_total_prof_2:.2f}R$,enquanto o professor 2 ganha {ganho_total_prof_1:.2f}R$ .'
  else: ganho_total_prof_1 == ganho_total_prof_2
  return f'Os dois professores ganham o mesmo {ganho_total_prof_1:.2f}R$'


def obter_numero_real(label: str):
  return float(input(label))


main()