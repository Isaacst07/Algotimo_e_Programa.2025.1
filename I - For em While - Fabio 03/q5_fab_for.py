def main():
    n = eh_inteiro('Digite um número: ')
    num = n
    contador = 1 
    soma = 1
    while n >= contador:
       soma *= n 
       n -= 1 
    
    print(f'O fatorial do número {num} é {soma} ')


def eh_inteiro(label):
    entrada = input(label)

    try:
     numero = int(entrada)
     return numero
    except ValueError:
       return eh_inteiro(label)


main()