import utils as b
import random


def inicializar_vetor():
    b.limpar_tela()

    menu = '''\tVocê quer ?
            1 - Vetor Automático
            2 - Adicionar Valores Manualmente
            3 - Carregar valores de um arquivo
            >>> '''

    escolha = b.obter_numero_da_faixa(menu, 1, 3)
            
    if escolha == 1:
        vetor = inicializar_vetor_automaticamente()
        b.finalizar()

        return vetor
            
    elif escolha == 2:
        vetor = inicializar_vetor_manualmente()
        b.finalizar()

        return vetor

    elif escolha == 3:
        vetor = inicializar_vetor_por_arquivo()
        b.finalizar()

        return vetor


def inicializar_vetor_manualmente():
    colecao = []
    minimo = b.obter_numero_inteiro('Faixa miníma dos valores do vetor: ')
    maximo = b.obter_numero_minimo('Faixa máxima dos valores do vetor: ', minimo)
    qtd_valores = b.obter_numero_minimo('Quantidade de valores a serem adicionados: ', 1)

    b.limpar_tela()

    for i in range(0, qtd_valores, 1):
        valor = b.obter_numero_da_faixa(f'{i}° Valor a ser adiconado: ', minimo, maximo)
        colecao.append(valor)
        b.limpar_tela()
    
    print('Valores Adiconados com sucesso!')

    return colecao


def inicializar_vetor_automaticamente():
    colecao = []
    minimo = b.obter_numero_inteiro('Faixa miníma dos valores do vetor: ')
    maximo = b.obter_numero_minimo('Faixa máxima dos valores do vetor: ', minimo)
    qtd_valores = b.obter_numero_minimo('Quantidade de valores a serem adicionados: ', 1)

    b.limpar_tela()

    for i in range(0, qtd_valores, 1):
        valor = random.randint(minimo, maximo)
        colecao.append(valor)
    
    print('Vetor gerado com sucesso!')

    return colecao


def inicializar_vetor_por_arquivo():
    colecao = []

    nome_arquivo = input('Nome do arquivo(Ex: nome.txt): ')

    arquivo = open(nome_arquivo)

    for linha in arquivo:
        item = linha.strip()
        colecao.append(item)
    
    print('Valores do arquivo foram adicionados com sucesso!')

    return colecao


def load_itens_do_vetor():
    vetor = []
    arquivo = open('banco_de_dados.txt')

    for linha in arquivo:
        valor = linha.strip()
        vetor.append(valor)
    
    print('Valores carregados no vetor com sucesso!')

    return vetor


def mostrar_todos_os_valores(colecao):
    for item in colecao:
        print(item)


def resetar_vetor():
    nova_colecao = []
    return nova_colecao


def maior_valor(colecao):
    posicao_maior = None
    maior = None

    for i in range(0, len(colecao), 1):
        if maior == None or colecao[i] > maior:
            posicao_maior = i
            maior = colecao[i]

    print(f'O maior valor é: {maior} na posição {posicao_maior}')


def menor_valor(colecao):
    posicao_menor = None
    menor = None

    for i in range(0, len(colecao), 1):
        if menor == None or colecao[i] < menor:
            posicao_menor = i
            menor = colecao[i]

    print(f'O maior valor é: {menor} na posição {posicao_menor}')


def reduzir(colecao, funcao_redutora, acumulado):
    
    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado


def filtrar(colecao, condicao):
    nova_colecao = []

    for item in colecao:
        if condicao(item): 
            nova_colecao.append(item)

    return nova_colecao


def mapear(colecao,funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)

    return nova_colecao


def subtistuir_valores_negativos(colecao, minimo, maximo):

    for i in range(0, len(colecao), 1):
        if colecao[i] < 0:
            colecao[i] = random.randint(minimo, maximo)

    return colecao


def ordenar(colecao):
    ordenar = b.obter_numero_da_faixa('Ordena de maneira crescente ou decrescente(Crescente = 1 / Decrencente = 2): ', 1, 2)

    if ordenar == 1:
        colecao.sort()
    else:
        colecao.sort(reverse=True)

    return colecao


def embaralhar(colecao):

    nova_colecao = []
    indexs = len(colecao) - 1

    for _ in range (len(colecao)):
        item_removido = colecao.pop(random.randint(0, indexs))
        nova_colecao.append(item_removido)
        indexs -= 1

    return nova_colecao


def adicionar_valores(colecao):

    valor = b.obter_numero_inteiro('Valor a ser adicionado: ')
    colecao.append(valor)

    return colecao


def remover_por_posicao(colecao, posicao_remover):
    nova_colecao = []

    for i in range(0, len(colecao), 1):
        if i != posicao_remover - 1:
            nova_colecao.append(colecao[i])

    return nova_colecao


def editar_valor_por_posicao(colecao, posicao_editar):
    print(f'O valor da posição {posicao_editar} é {colecao[posicao_editar - 1]}')
    colecao[posicao_editar - 1] = b.obter_numero_inteiro('Novo valor da posição: ')

    return colecao


def salvar(colecao, nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    linha_do_arquivo = ''

    for item in colecao:
        linha_do_arquivo += f'{item}\n'

    arquivo.write(linha_do_arquivo)