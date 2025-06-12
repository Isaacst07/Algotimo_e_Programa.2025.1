from funcoes import obter_numero_inteiro
from funcoes import limpar_tela
from funcoes import obter_numero_real

def main():
    n = obter_numero_inteiro('Quantos números n a lista vai ter: ')
    contador = 1 
    somatorio = 0 

    while contador <= n:
        num = obter_numero_real('Digite um número: ')
        limpar_tela()
        contador += 1 
        somatorio += num

    print(f'A soma dos n números da lista é {somatorio} e a média é {(somatorio / n):.2f}')


main()