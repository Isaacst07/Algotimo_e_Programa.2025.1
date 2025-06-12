def main():
   numero_1 = obter_numero_inteiro('Digite um numero inteiro: ')
   numero_2 = obter_numero_inteiro('Digite outro número inteiro: ')
   opcao = obter_numero_interio_min('Digite umas das opções (1/2/3/4): ')

   Oq_fazer(numero_1, numero_2, opcao)



def Oq_fazer(numero_1, numero_2, opcao):
  if opcao == 1:
    return print(f'A opçaõ escolhida foi a 1, então se soma os números,que é igual {numero_1 + numero_2} .')
  elif opcao == 2: 
    return print(f'A opçaõ escolhida foi a 2, então se subtrai os números,que é igual {numero_1 - numero_2} .')
  elif opcao == 3: 
    return print(f'A opçaõ escolhida foi a 3, então se multiplica os números,que é igual {numero_1 * numero_2} .')
  else: opcao == 4
  return print(f'A opção escolhida foi a 4, então se divide os valores,que é igual {numero_1 / numero_2:.2f} .')
  

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
  min = 1
  max = 4
  if  min <= numero <= max:
    return numero
  else:
    print(f'A opção escolhida deve ser entre 1, 2, 3 ou 4')
    return print(obter_numero_interio_min(label))


main()