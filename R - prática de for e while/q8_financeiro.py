import os


def main():
    limpar_tela()

    print('Olá, vamos ajudar você no seu controle financeiro!')
    dar_espaco()

    receitas = obter_numero_int('Quantidade de receitas a analisar: ')
    total_receitas = 0
    maior_receita = 0
    descricao_maior_receita = None 

    for i in range (1, receitas + 1, 1):
        limpar_tela()
        print(f'--------{i}° RECEITA--------')
        valor_receita = obter_numero_float('Qual o valor da receita(R$): ')
        descricao_receita = str(input('Descrição da receita: '))

        total_receitas += valor_receita

        if maior_receita == 0 or valor_receita > maior_receita:
            maior_receita = valor_receita
            descricao_maior_receita = descricao_receita

        input('Enter to continue...')

    limpar_tela()
    despesas = obter_numero_int('Quantidade de despesas(R$): ')
    total_despesas = 0
    maior_despesa = 0 
    descricao_maior_despesa = None

    for i in range (1, despesas + 1, 1):
        limpar_tela()
        print(f'--------{i}° DESPESA--------')
        valor_despesa = obter_numero_float('Qual o valor da receita(R$): ')
        descricao_despesa = str(input('Descrição da receita: '))

        total_despesas += valor_despesa

        if maior_despesa == 0 or valor_despesa > maior_despesa:
            maior_despesa = valor_despesa
            descricao_maior_despesa = descricao_despesa

        input('Enter to continue...')

    limpar_tela()
    
    print(f'''-----------RESUMO FINANCEIRO-----------
a) Total de receitas do mês: R$ {total_receitas:.2f} 
b) Total de despesas do mês: R$ {total_despesas:.2f} 
c) Saldo final do mês: R$ {(total_receitas - total_despesas):.2f}
d) Maior receita: R$ {maior_receita:.2f} - {descricao_maior_receita}
d) Maior despesa: R$ {maior_despesa:.2f} - {descricao_maior_despesa}

''')
        

def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um interio válido!')
        obter_numero_int(label)


def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um numero válido!')
        obter_numero_float(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()