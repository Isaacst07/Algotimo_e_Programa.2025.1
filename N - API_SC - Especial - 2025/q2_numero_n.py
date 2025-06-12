# (q2_numero_n.py) Dado um número inteiro N, e N sequências de
# números inteiros terminadas por 0, calcular e imprimir:
# a. A soma dos números pares de cada sequência.
# b. A média de todos os números digitados de todas as
# sequências.
# c. O menor e o maior números digitados de todas as sequências.

# Domingo
# comecei 12:56
# terminei 13:26

from q1_number_utils import obter_numero_inteiro
from q1_number_utils import limpar_tela


def main():
    n = obter_numero_inteiro('Digite o número de sequências: ')
    soma_pares = 0 
    somatorio = 0 
    qtd_num = 0 
    maior_num = ''
    menor_num = ''
    contador = 1

    while contador <= n:
            limpar_tela()
            print(f'{contador}° Sequencia:')
            print('')

            while True:
                n_sequencia = obter_numero_inteiro('Digite um número N da sequência(0 == PARAR): ')

                if n_sequencia == 0:
                    break

                somatorio += n_sequencia
                qtd_num += 1
                
                if maior_num == '' or n_sequencia > maior_num :
                    maior_num = n_sequencia

                if menor_num == '' or n_sequencia < menor_num :
                    menor_num = n_sequencia
                    
                if n_sequencia % 2 == 0:
                    soma_pares += n_sequencia

            contador += 1
    
    print(f'''
a. A soma dos números pares de cada sequência: {soma_pares}
b. A média de todos os números digitados de todas as sequências: {(somatorio / qtd_num):.2f}
c. O menor digitado da sequência: {menor_num}
d. O maior digitado da sequência: {maior_num}

''')
    

    print('Fim!')


main()    