def main():
    n = eh_inteiro('N: ')
    contador = 1

    while contador <= n:
        if contador % 2 == 0:
         print(f'{contador}')
        contador += 1 
       

def eh_inteiro(label):
  entrada = input(label)

  try:
    numero = int(entrada)
    return numero
  except ValueError:
   print('O valor escolhido não é um inteiro válido ')
   eh_inteiro(label)


main()