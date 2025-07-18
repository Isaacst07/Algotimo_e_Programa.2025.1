import utils as u
import vetor_utils as i


def main():
    u.limpar_tela()

    vetor = []

    print('Óla, vamos iniciar o vetor!')
    print()
    escolha = u.obter_numero_da_faixa('Você quer inicializar ou fazer load do vetor(sim = 1(Inicilizar vetor) / não = 0 (Fazer load)): ',0, 1)

    if escolha == 1:
        vetor = i.inicializar_vetor()
    else:
        vetor = i.load_itens_do_vetor()
    
    while True:

        opcao = u.chamar_menu()

        if opcao == 1:
            u.limpar_tela()
            i.mostrar_todos_os_valores(vetor)
            u.finalizar()

        elif opcao == 2:
            vetor = i.resetar_vetor()
            print('Vetor resetado com sucesso!')
            u.finalizar()

        elif opcao == 3:
            u.limpar_tela()
            print(f'Quantidade de itens no vetor: {len(vetor)}')
            u.finalizar()

        elif opcao == 4:
            u.limpar_tela()
            i.maior_valor(vetor)
            i.menor_valor(vetor)
            u.finalizar()

        elif opcao == 5:
            u.limpar_tela()
            somatorio = i.reduzir(vetor, u.somar, 0 )
            print(f'A soma dos valores é igual: {somatorio}')
            u.finalizar()

        elif opcao == 6:
            u.limpar_tela()
            media = i.reduzir(vetor, u.somar, 0) / (len(vetor))
            print(f'A média dos valores é: {media:.2f}')
            u.finalizar()

        elif opcao == 7:
            u.limpar_tela()
            positivos = i.filtrar(vetor, lambda item:item > 0)
            for positivo in positivos:
                print(positivo)
            
            print()
            print(f'A quantidade de valores positivos é: {len(positivos)}')
            u.finalizar()

        elif opcao == 8:
            u.limpar_tela()
            negativos = i.filtrar(vetor, lambda item:item < 0)
            for negativo in negativos:
                print(negativo)

            print()
            print(f'A quantidade de valores negativos é: {len(negativos)}')
            u.finalizar()

        elif opcao == 9:
            u.limpar_tela()
            
            regra = u.regra_opcao_9()

            if regra == 1:
                u.limpar_tela()
                valor = u.obter_numero_inteiro('Valor para multiplicar: ')
                vetor = i.mapear(vetor, lambda item:item*valor)
                print('Valores atulizado com sucesso!')
                u.finalizar()

            elif regra == 2:
                u.limpar_tela()
                expoente = u.obter_numero_inteiro('Valor do expoente: ')
                vetor = i.mapear(vetor, lambda item:item**expoente)
                print('Valores atualizado com sucesso!')
                u.finalizar()

            elif regra == 3:
                u.limpar_tela()
                numerador, denominador = map(int, input('Fração (Ex:x/y): ').split('/'))
                vetor = i.mapear(vetor, lambda item:item * (numerador / denominador))
                print(f'Valores reduzidos pela fração {numerador}/{denominador} com sucesso!')
                u.finalizar()

            elif regra == 4:
                u.limpar_tela()
                minimo = u.obter_numero_inteiro('Faixa mínima: ')
                maximo = u.obter_numero_minimo('Faixa máximo: ', minimo)
                vetor = i.subtistuir_valores_negativos(vetor, minimo, maximo)
                print('Valores negativos atualizados com sucesso!')
                u.finalizar()
            
            elif regra == 5:
                u.limpar_tela()
                u.limpar_tela()
                vetor = i.ordenar(vetor)
                print('Vetor Ordenado com sucesso!')
                u.finalizar()

            elif regra == 6:
                u.limpar_tela()
                vetor = i.embaralhar(vetor)
                print('Vetor Atualizado com sucesso!')
                u.finalizar()

        elif opcao == 10:
            u.limpar_tela()
            vetor = i.adicionar_valores(vetor)
            print('Valor adicionado com sucesso!')
            u.finalizar()

        elif opcao == 11:
            u.limpar_tela()
            print(vetor)
            valor_removido = u.obter_numero_inteiro('Qual Valor da lista você vai remover: ')
            vetor = i.filtrar(vetor, lambda item:item != valor_removido)
            print(f'O valor {valor_removido} foi removido com sucesso!')
            u.finalizar()

        elif opcao == 12:
            u.limpar_tela()
            print(vetor)
            posicao_remover = u.obter_numero_da_faixa('Qual a posição a ser removida: ', 1, len(vetor))
            vetor = i.remover_por_posicao(vetor,posicao_remover)
            print(f'Item na posição {posicao_remover} foi removido com sucesso!')
            u.finalizar()

        elif opcao == 13:
            u.limpar_tela()
            print(vetor)
            posicao_editar = u.obter_numero_da_faixa('Qual a posição do valor para editar: ', 1, len(vetor))
            vetor = i.editar_valor_por_posicao(vetor, posicao_editar)
            print(f'Valor editado com sucesso!')
            u.finalizar()

        elif opcao == 14:
            u.limpar_tela()
            nome_arquivo = input('Nome do arquivo para salvar(Ex: nome_arq.txt): ')
            i.salvar(vetor, nome_arquivo)
            print('Salvo com sucesso!')
            u.finalizar()

        elif opcao == 0:
            break
    
    u.limpar_tela()

    i.salvar(vetor, 'banco_de_dados.txt')
    print('Salvo com sucesso!')


main()