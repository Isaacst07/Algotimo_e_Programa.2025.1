def main():
    dia_1 = obter_numero_interio_min_dia('Digite o dia da primeira data: ')
    mes_1 = obter_numero_interio_min_mes('Digite o mês da primeira data: ')
    ano_1 = obter_numero_inteiro('Digite o ano da primira data: ')
    dia_2 = obter_numero_interio_min_dia('Digite o dia da segunda data: ')
    mes_2 = obter_numero_interio_min_mes('Digite o mês da segunda data: ')
    ano_2 = obter_numero_inteiro('Digite o ano da terceira data: ')

    data_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)

   
def data_recente(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):
   if ano_1 > ano_2:
      return print(f'A data {dia_1}/{mes_1}/{ano_1} é mais recente que a data {dia_2}/{mes_2}/{ano_2}')
   elif ano_2 > ano_1:
      return print(f'A data {dia_2}/{mes_2}/{ano_2} é mais recente que a data {dia_1}/{mes_1}/{ano_1}')
   elif ano_1 == ano_2 and mes_1 > mes_2:
      return print(f'A data {dia_1}/{mes_1}/{ano_1} é mais recente que a data {dia_2}/{mes_2}/{ano_2}')
   elif ano_2 == ano_1 and mes_2 > mes_1:
      return print(f'A data {dia_2}/{mes_2}/{ano_2} é mais recente que a data {dia_1}/{mes_1}/{ano_1}')
   elif ano_1 == ano_2 and mes_1 == mes_2 and dia_1 > dia_2:
      return print(f'A data {dia_1}/{mes_1}/{ano_1} é mais recente que a data {dia_2}/{mes_2}/{ano_2}')
   elif ano_2 == ano_1 and mes_2 == mes_1 and dia_2 > dia_1:
      return print(f'A data {dia_2}/{mes_2}/{ano_2} é mais recente que a data {dia_1}/{mes_1}/{ano_1}')
   else: ano_1 == ano_2 and mes_1 == mes_2 and ano_1 == ano_2
   return print(f'As datas {dia_1}/{mes_1}/{ano_1} e {dia_2}/{mes_2}/{ano_2} são iguais')


def obter_numero_interio_min_dia(label:str ):
  numero = obter_numero_inteiro(label)
  min = 1
  max = 31
  if  min <= numero <= max:
    return numero
  else:
    print(f'Digite um dia válido de 1 a 31')
    return print(obter_numero_interio_min_dia(label))
  

def obter_numero_interio_min_mes(label:str ):
  numero = obter_numero_inteiro(label)
  min = 1
  max = 12
  if  min <= numero <= max:
    return numero
  else:
    print(f'Digite um mês válido ou mês 1 ou mês 2 ...')
    return print(obter_numero_interio_min_mes(label))
  
    
def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()