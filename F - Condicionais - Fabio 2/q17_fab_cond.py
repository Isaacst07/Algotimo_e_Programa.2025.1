def main():
   numero_1 = obter_numero_inteiro('Digite um numero inteiro: ')
   numero_2 = obter_numero_inteiro('Digite outro número inteiro: ')

   opcao_1 = numero_1 + numero_2 + 1
   opcao_2 = eh_par(numero_1, numero_2)
   opcao_3 = (numero_1 + numero_2) * numero_1
   opcao_4 = (numero_1 + numero_2) / numero_2 
   quadrado_1 = numero_1 ** 2
   quadrado_2 = numero_2 ** 2 

   resto_da_divisão(numero_1, numero_2, opcao_1, opcao_2, opcao_3, opcao_4, quadrado_1, quadrado_2)


def resto_da_divisão(numero_1, numero_2, opcao_1, opcao_2, opcao_3, opcao_4, quadrado_1, quadrado_2):
  if numero_1 % numero_2 == 1:
    return print(f'O resto da divisão dos dois números foi igual a 1,então somasse os dois mais o resto da divisão que é igual a {opcao_1}')
  elif numero_1 % numero_2 == 2:
    return print(f'O resto da divisão dos dois números foi igual a 2,então {opcao_2}')  
  elif numero_1 % numero_2 == 3:
    return print(f'O resto da divisão dos dois números foi igual a 3,então multiplicasse a soma dos números pelo primeiro que é igual a {opcao_3}')
  elif numero_1 % numero_2 == 4:
    return print(f'O resto da divisão dos dois números foi igual a 4,então divide a soma dos números pelo  que é igual a {opcao_4}') 
  else:
    return print(f'O resto da divisão não foi nenhuma das anteriores,então se calcula o quadrado dos numeros, que são respectivamente {quadrado_1} e {quadrado_2}') 


def eh_par(numero_1, numero_2):
  if numero_1 / 2 == 0 and numero_2 / 2 == 0:
    return f'Os números {numero_1} e {numero_2} são PARES!'
  elif numero_1 / 2 == 0 and numero_2 / 2 != 0:
    return f'O número {numero_1} é PAR e o número {numero_2} é ÍMPAR'
  elif numero_1 / 2 != 0 and numero_2 / 2 == 0:
    return f'O número {numero_2} é PAR e o número {numero_1} é ÍMPAR'
  else: 
    return f'Os números {numero_1} e 5{numero_2} são ÍMPARES!'
  

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()