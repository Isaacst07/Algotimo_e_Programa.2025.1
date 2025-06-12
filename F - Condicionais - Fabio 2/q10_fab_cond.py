def main():
    dia = obter_numero_inteiro('Digite o dia da data desejada: ')
    mes = obter_numero_inteiro('Digite o mês da data desejada: ')
    ano = obter_numero_inteiro('Digite o ano da data desejada: ')

    print(validar_data(dia, mes, ano))
          


def validar_mes(mes):
   if 1 <= mes <=12:
      return True
   else:
      False


def validar_dia(dia, mes):
    if mes in (1, 3, 5, 7, 8, 10, 12) and 1 <= dia <= 31:
      return True
    elif mes in (4, 6, 9, 11) and 1 <= dia <= 30:
      return True
    elif mes == 2 and 1 <= dia <= 28:
      return True
    else:
       False


def validar_data(dia, mes, ano):
   if validar_mes(mes) == True and validar_dia(dia, mes) == True:
      return f'A data {dia}/{mes}/{ano} é VÁLIDA!'
   else:
      return f'A data {dia}/{mes}/{ano} NÃO é válida'


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()