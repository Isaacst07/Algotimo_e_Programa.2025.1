def main():
    numero = obter_numero_interio_min('Digite um número de 4 dígitos: ')

    quadrado_eh_igual_original(numero)


def quadrado_eh_igual_original(numero):
    parte_um_numero = numero // 100
    parte_dois_numero = numero % 100
    if (parte_um_numero + parte_dois_numero) ** 2 == numero:
       return print(f'Esse número é especial dentre os de 4 digítos,pois o quadrado de sua primera parte {parte_um_numero} mais a segunda parte {parte_dois_numero} é igual a {(parte_um_numero + parte_dois_numero) ** 2} que é ele mesmo {numero}')
    else: 
       return print(f'Esse número NÃO é especial dentre os de 4 digítos,pois o quadrado da primera parte {parte_um_numero} mais a segunda parte {parte_dois_numero} é igual a {(parte_um_numero + parte_dois_numero) ** 2} que NÃO é igual a ele mesmo {numero}')


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
  min = 1000
  max = 9999
  if  min <= numero <= max:
    return numero
  else:
    print(f'O valor escolhido por ser de 4 dígitos deve ser entre {min} e {max}')
    return print(obter_numero_interio_min(label))


main()

