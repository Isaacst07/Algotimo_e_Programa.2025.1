def main():
    dia_atual = obter_numero_inteiro('Digite o dia atual: ')
    mes_atual = obter_numero_inteiro('Digite o mês atual: ')
    ano_atual = obter_numero_inteiro('Digite o ano atual: ')
    dia_nascimento = obter_numero_inteiro('Digite o dia do seu nascimento: ')
    mes_nascimento = obter_numero_inteiro('Digite o mês do seu nascimento: ')
    ano_nascimento = obter_numero_inteiro('Digite o ano do seu nascimento: ')

    if validar_ano(ano_atual, ano_nascimento) and validar_mes(mes_atual, mes_nascimento):
      
       if not validar_data(dia_atual, mes_atual):
          print(f'Digite a data atual válida: {dia_atual}/{mes_atual}/{ano_atual}')
       if not validar_data(dia_nascimento, mes_nascimento):
          print(f'Digite uma data de nascimento válida: {dia_nascimento}/{mes_nascimento}/{ano_nascimento}')
       if validar_data(dia_atual, mes_atual) and validar_data(dia_nascimento, mes_nascimento):
          print(f'A data atual: {dia_atual}/{mes_atual}/{ano_atual}')
          print(f'A sua data de nascimento: {dia_nascimento}/{mes_nascimento}/{ano_nascimento}')
          calcular_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)

def validar_ano(ano_atual, ano_nascimento):
   return ano_atual >= 1 and ano_nascimento >= 1


def validar_mes(mes_atual, mes_nascimento):
   return 1 <= mes_atual <=12 and 1 <= mes_nascimento <=12


def validar_data(dia, mes):
   ano = 365
   if mes in (1, 3, 5, 7, 8, 10, 12):
      return 1 <= dia <= 31
   elif mes in (4, 6, 9, 11):
      return 1 <= dia <= 30
   else: mes == 2 
   return 1 <= dia <= 28


def calcular_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento):
   idade_anos = ano_atual - ano_nascimento
   idade_mes = mes_atual - mes_nascimento
   idade_dias = dia_atual - dia_nascimento

   if idade_dias < 0:
      idade_dias += dia_nascimento
      idade_mes -= 1

   if idade_mes < 0:
      idade_mes += 12 
      idade_anos -= 1 
   print(f'Idade é igual {idade_anos} anos, {idade_mes} meses e {idade_dias} dias !') 
    
def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()