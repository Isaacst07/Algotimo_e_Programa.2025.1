from funcoes import obter_numero_inteiro
from funcoes import obter_numero_real
from funcoes import limpar_tela


def main():
    n = obter_numero_inteiro('Quantos números N tem na lista: ')
    contador = 1
    maior = None

    while contador <= n:
        num = obter_numero_real('Digite um número: ')

        if maior is None or num > maior:
            maior = num
        
        limpar_tela()
        contador += 1 
    
    print(f'O maior número digitado da lista foi: {maior}')
        





main()