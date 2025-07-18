import utils as u
import vetor as v 
#15640

def main():
    u.limpar_tela()
    escolas = v.inicializar_sistema()
    
    while True:
        u.limpar_tela()

        opcao = v.menu()

        if opcao == 0:
            break

        elif opcao == 1:
            u.limpar_tela()
            n = u.obter_numero_da_faixa('Top Brasil(N): ', 1, 15640)
            v.top_n_brasil(escolas, n)
            u.finalizar()

        elif opcao == 2:
            u.limpar_tela()
            v.top_n_brasil_por_area(escolas)
            u.finalizar()

        elif opcao == 3:
            u.limpar_tela()
            estado = input('Estado(Ex: PI): ').upper()
            n_estado = u.obter_numero_da_faixa('Top Brasil(N): ', 1, 15640)
            v.top_n_por_estado(escolas, estado, n_estado)
            u.finalizar()

        elif opcao == 4:
            u.limpar_tela()
            v.top_n_por_estado_e_rede(escolas)
            u.finalizar()

        elif opcao == 5:
            u.limpar_tela()
            menu = '''-------ÁREA DO CONHECIMENTO-------
    1 - Linguagens 
    2 - Matemática
    3 - Ciência da Natureza
    4 - Ciências Humanas
    5 - Redação

    >>> '''

            area = u.obter_numero_da_faixa(menu, 1, 5)
            v.media_nacional_por_area(escolas, area)
            u.finalizar()
        
        elif opcao == 6:
            u.limpar_tela()
            menu = '''-------ÁREA DO CONHECIMENTO-------
    1 - Linguagens 
    2 - Matemática
    3 - Ciência da Natureza
    4 - Ciências Humanas
    5 - Redação

    >>> '''

            area = u.obter_numero_da_faixa(menu, 1, 5)

            v.melhor_escola_por_area_estado_ou_br(escolas, area)
            u.finalizar()

        elif opcao == 7:
            u.limpar_tela()
            v.listar_escolas_por_estado_renda(escolas)
            u.finalizar()

        elif opcao == 8:
            u.limpar_tela()
            v.busca_especifica(escolas)
            u.finalizar()

        elif opcao == 9:
            u.limpar_tela()
            v.ranking_por_estado(escolas)
            u.finalizar()
            

main()