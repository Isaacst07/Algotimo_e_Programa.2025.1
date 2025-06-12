# comecei 11:04
# terminei 12:01
# Domingo

from q1_number_utils import obter_numero_inteiro_entre_faixa
from q1_number_utils import obter_numero_inteiro
from q1_number_utils import limpar_tela


def main():
    
    menu = '''-----------MENU-----------
1 - Para inserir produtos;

    produtos: 
    cerveja (C) - R$ 9.00
    Tira gosto (T) - R$ 39.00
    Água (A) - R$ 5.00

2 - Para calcular conta;
'''

    total_cerveja = 0
    total_tira_gosto = 0
    total_agua = 0 

    while True:
        limpar_tela()
        print(f'{menu}')
        operacao = obter_numero_inteiro_entre_faixa('Digite o numero da operação desejada: ', 1, 2)

        
        if operacao == 1:
            produto = input('Produto a ser inserido(Ex: 1 C -> 1 Cerveja): ')
            qtd_produto = int(produto.split() [0])
            tipo_produto = produto.split() [1]
            if tipo_produto.upper() == 'C':
                total_cerveja += qtd_produto
                if tipo_produto.upper() == 'T':
                    total_tira_gosto += qtd_produto
                    if tipo_produto.upper() == 'A':
                        total_agua += qtd_produto
        
        limpar_tela()


        if operacao == 2:
            qtd_pessoas = obter_numero_inteiro('Quantidade de pessoas que irão pagar: ')
            conta = calcular_conta(total_cerveja, total_tira_gosto, total_agua, qtd_pessoas)
            print(f'{conta}')

            print('')

            input('Aperte <Enter> para confirmar pagamento ...')

            limpar_tela()

            break 

    print('Pagamento confirmado volte sempre!')


def calcular_conta(total_cervejas: int, total_tira_gosto: int, total_agua: int, qtd_pessoas: int):
    valor_total_cerveja = total_cervejas * 9 
    valor_total_tira_gosto = total_tira_gosto * 39
    valor_total_agua = total_agua * 5
    valor_total_conta = valor_total_cerveja + valor_total_tira_gosto + valor_total_agua

    if valor_total_conta > 200 or total_cervejas > 10:
        conta = f'''-------------------> CONTA <-------------------
1) Valor total da conta: R$ {valor_total_conta:.2f}
2) Valor por pessoa: R$ {(valor_total_conta / qtd_pessoas):.2f}
3) Valor total com taxa de serviço : R$ {valor_total_conta:.2f}

        '''
        return conta

    else:
        taxa_de_serviço = valor_total_conta * 0.1
        valor_total_com_taxa = valor_total_conta + taxa_de_serviço
        conta = f'''-------------------> CONTA <-------------------
1) Valor total da conta: R$ {valor_total_conta:.2f}
2) Valor por pessoa: R$ {(valor_total_com_taxa / qtd_pessoas):.2f}
3) Valor total com taxa de serviço : R$ {valor_total_com_taxa:.2f}

        '''
        return conta


main()