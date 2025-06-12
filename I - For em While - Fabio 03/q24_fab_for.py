import funcoes

def main():
    habitantes = funcoes.obter_numero_inteiro('Números de Habitantes: ')
    pesq_habitantes(habitantes)


def pesq_habitantes(habitantes):
    contador = 1 
    soma_salario = 0
    soma_filhos = 0 
    percentual = 0 

    while contador <= habitantes:
        funcoes.limpar_tela()
        print(f'----------HABITANTE {contador}----------')
        salario = funcoes.obter_numero_real('Salário do habitante: ')
        filho = funcoes.obter_numero_inteiro('Número de filhoes desse habitante: ')

        if salario <= 1000:
            percentual += 1

        soma_salario += salario
        soma_filhos += filho 
        contador += 1 
    funcoes.limpar_tela()
    print(f'''
a) média de salário da população: {(soma_salario / habitantes):.2f} R$
b) média de número de filhos: {int(soma_filhos / habitantes)} filhos por habitantes.
c) percentual de pessoas com salário de até R$ 1.000,00: {((percentual / habitantes) * 100):.2f}%

''')


main()