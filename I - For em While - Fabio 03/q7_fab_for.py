from funcoes import obter_numero_inteiro

def main(): 

    n = obter_numero_inteiro ('N: ')
    contador = 1
    soma = 0
 
    while contador <= n:
            soma += contador
            contador += 1

    print(f'A soma de 1 até {n} é igual a {soma}')
   

main()