from funcoes import obter_numero_inteiro
def main():
  numero_1 = obter_numero_inteiro('Digite número: ')
  numero_2 = obter_numero_inteiro('Digite número: ')
  numero_3 = obter_numero_inteiro('Digite número: ')
  opcao_num = obter_numero_inteiro('Digite uma opção entre(1/2/3): ')

  print('opcao_numero(numero_1, numero_2, numero_3, opcao_num)')


def opcao_numero(numero_1, numero_2, numero_3, opcao_num):
  if opcao_num == 1:
   return f'{numero_1}'
  elif opcao_num == 2:
   return f'{numero_2}'
  if opcao_num == 3:
   return f'{numero_3}'


main()