def main():
   numero_1 = obter_numero_inteiro('Digite o primeiro número: ')
   numero_2 = obter_numero_inteiro('Digite o segundo número: ')
   numero_3 = obter_numero_inteiro('Digite o terceiro número: ')

   print(ordem_crescente(numero_1, numero_2, numero_3))


def ordem_crescente(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 and numero_1 > numero_3 and numero_2 > numero_3:
        return (f'Em ordem crescente {numero_3}, {numero_2}, {numero_1} . ')
    elif numero_1 > numero_2 and numero_1 > numero_3 and numero_3 > numero_2:
        return (f'Em ordem crescente {numero_2}, {numero_3}, {numero_1} . ')
    elif numero_2 > numero_1 and numero_2 > numero_3 and numero_1 > numero_3:
        return (f'Em ordem crescente {numero_3}, {numero_1}, {numero_2} . ')
    elif numero_2 > numero_1 and numero_2 > numero_3 and numero_3 > numero_1:
        return (f'Em ordem crescente {numero_1}, {numero_3}, {numero_2} . ')
    elif numero_3 > numero_1 and numero_3 > numero_2 and numero_1 > numero_2:
        return (f'Em ordem crescente {numero_2}, {numero_1}, {numero_3} . ')
    else: numero_3 > numero_1 and numero_3 > numero_2 and numero_2 > numero_1
    return (f'Em ordem crescente {numero_1}, {numero_2}, {numero_3} . ')
        

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)


main()