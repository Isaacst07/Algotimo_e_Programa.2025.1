def main():
    numero_1 = obter_numero_inteiro('Digite o primeiro número: ')
    numero_2 = obter_numero_inteiro('Digite o segundo número: ')
    numero_3 = obter_numero_inteiro('Digite o segundo número: ')
    numero_4 = obter_numero_inteiro('Digite o segundo número: ')
    numero_5 = obter_numero_inteiro('Digite o segundo número: ')

    eh_maior(numero_1, numero_2, numero_3, numero_4, numero_5) 
    eh_menor(numero_1, numero_2, numero_3, numero_4, numero_5) 


def eh_maior(numero_1, numero_2, numero_3, numero_4, numero_5):
    if numero_1 > numero_2 and numero_1 > numero_3 and numero_1 > numero_4 and numero_1 > numero_5:
        return print(f'{numero_1} é o MAIOR entre os números! ')
    elif numero_2 > numero_1 and numero_2 > numero_3 and numero_2 > numero_4 and numero_2 > numero_5:
        return print(f'{numero_2} é o MAIOR entre os números! ')
    elif numero_3 > numero_1 and numero_3 > numero_2 and numero_3 > numero_4 and numero_3 > numero_5:
        return print(f'{numero_3} é o MAIOR entre os números! ')
    elif numero_4 > numero_1 and numero_4 > numero_2 and numero_4 > numero_3 and numero_4 > numero_5:
        return print(f'{numero_4} é o MAIOR entre os números! ')
    else: numero_5 > numero_1 and numero_5 > numero_2 and numero_5 > numero_3 and numero_5 > numero_4
    return print(f'{numero_5} é o MAIOR entre os números! ')


def eh_menor(numero_1, numero_2, numero_3, numero_4, numero_5):
   if numero_1 < numero_2 and numero_1 < numero_3 and numero_1 < numero_4 and numero_1 < numero_5:
        return print(f'E o  {numero_1} é o MENOR entre os números! ')
   elif numero_2 < numero_1 and numero_2 < numero_3 and numero_2 < numero_4 and numero_2 < numero_5:
        return print(f'E o {numero_2} é o MENOR entre os números! ')
   elif numero_3 < numero_1 and numero_3 < numero_2 and numero_3 < numero_4 and numero_3 < numero_5:
        return print(f'E o {numero_3} é o MENOR entre os números! ')
   elif numero_4 < numero_1 and numero_4 < numero_2 and numero_4 < numero_3 and numero_4 < numero_5:
        return print(f'E o {numero_4} é o MENOR entre os números! ')
   else: numero_5 < numero_1 and numero_5 < numero_2 and numero_5 < numero_3 and numero_5 < numero_4
   return print(f'E o {numero_5} é o MENOR entre os números! ')
    

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()