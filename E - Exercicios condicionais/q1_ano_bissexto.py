def main():
    ano = obter_numero_inteiro('Digite o ano: ')
    
    if eh_bissexto(ano):
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} NÃO é bissexto!')


def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()