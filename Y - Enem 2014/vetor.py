import utils as u

def inicializar_sistema():
    escolas = []
    arquivo_enem = open('enem-2014.csv')

    
    for linha in arquivo_enem:
        dados = linha.strip().split(';')
        escola = {}

        escola['ranking'] = dados[0]
        escola['nome'] = dados[1]
        escola['municipio'] = dados[2]
        escola['uf'] = dados[3]
        escola['rede'] = dados[4]
        escola['permanencia'] = dados[5]
        escola['nivel_socio_economico'] = dados[6]
        escola['media_objetivas'] =  dados[7]
        escola['linguagens'] = dados[8].replace(',','.')
        escola['matematica'] = dados[9].replace(',','.')
        escola['ciencias_natureza'] = dados[10].replace(',','.')
        escola['humanas'] = dados[11].replace(',','.')
        escola['redacao'] = dados[12].replace(',','.')

        escolas.append(escola)

    return escolas


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)

    return nova_colecao


def filtrar(colecao, funcao_condicional):
    nova_colecao = []

    for item in colecao:
        if funcao_condicional(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, funcao_redutora, acumulado):

    for item in colecao:
        acumulado = funcao_redutora(item, acumulado)

    return acumulado 


def top_n_brasil(colecao, n):
    
    print('Ranking das escolas brasileiras Enem 2014:\n')

    for i in range(0, n, 1):
        escola = colecao[i]
        
        print(f'{escola['ranking']}° - {escola['nome']} - {escola['rede']} - {escola['media_objetivas']}')


def menu():
    menu = '''============== Minerar Dados Enem 2014 ==============
    1 - Top N Brasil(todas as áreas)
    2 - Top N Brasil por Área 
    3 - Top N por Estado
    4 - Top N por Estado e Rede(Pública ou Privada)
    5 - Média Nacional por Área 
    6 - Melhor escola por Área e Estado ou BR
    7 - Listas Escolas por Estado Ordenado Por Renda
    8 - Busca escola específica por parte (Nome)
    9 - Ranking Enem por Estado
    10 - Ranking Enem por Região do País

    0 - Sair
    >>> '''

    opcao = u.obter_numero_da_faixa(menu, 0, 9)


    return opcao

def top_n_brasil_por_area(colecao):
    menu = '''-------ÁREA DO CONHECIMENTO-------
    1 - Linguagens 
    2 - Matemática
    3 - Ciência da Natureza
    4 - Ciências Humanas
    5 - Redação

    >>> '''

    area = u.obter_numero_da_faixa(menu, 1, 5)
    n  = u.obter_numero_da_faixa('Top Brasil(N): ', 1, 15640)

    if area == 1:
        escolas_ordenadas = sorted(colecao, key=lambda item:item['linguagens'], reverse=True)

        print(f'---------TOP {n} DO BRASIL EM LINGUAGENS---------\n')

        for i in range(0, n, 1):
            escola = escolas_ordenadas[i]

            print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['linguagens']}')

    elif area == 2:
        escolas_ordenadas = sorted(colecao, key=lambda item:item['matematica'], reverse=True)

        print(f'---------TOP {n} DO BRASIL EM MATEMÁTICA---------\n')

        for i in range(0, n, 1):
            escola = escolas_ordenadas[i]

            print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['matematica']}')

    elif area == 3:
        escolas_ordenadas = sorted(colecao, key=lambda item:item['ciencias_natureza'], reverse=True)

        print(f'---------TOP {n} DO BRASIL EM CIÊNCIAS DA NATUREZA---------\n')

        for i in range(0, n, 1):
            escola = escolas_ordenadas[i]

            print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['ciencias_natureza']}')

    elif area == 4:
        escolas_ordenadas = sorted(colecao, key=lambda item:item['humanas'], reverse=True)

        print(f'---------TOP {n} DO BRASIL EM CIÊNCIAS HUMANAS---------\n')

        for i in range(0, n, 1):
            escola = escolas_ordenadas[i]

            print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['humanas']}')

    elif area == 5:
        escolas_ordenadas = sorted(colecao, key=lambda item:item['redacao'], reverse=True)

        print(f'---------TOP {n} DO BRASIL EM REDAÇÃO---------\n')

        for i in range(0, n, 1):
            escola = escolas_ordenadas[i]

            print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['redacao']}')


def top_n_por_estado(colecao, estado, n):

    escola_do_estado = filtrar(colecao, lambda item:item['uf'] == estado)

    print(f'--------TOP {n} ESCOLAS DO {estado.upper()}--------')

    for i in range(0, n, 1):
        escola = escola_do_estado[i]

        print(f'{i+1}° - {escola['nome']} - {escola['media_objetivas']}')


def top_n_por_estado_e_rede(colecao):

    top = u.obter_numero_da_faixa('Top Brasil(N): ', 1, 15640)
    estado = input('Estado(Ex: PI): ').upper()
    rede = input('Rede(Ex: privada ou municipal): ').title()

    escolas_estado = filtrar(colecao, lambda escola: escola['uf'] == estado)
    escolas_rede = filtrar(escolas_estado, lambda escola: escola['rede'] == rede)


    if len(escolas_rede) < top:
        print(f'Perdão mais o Top N {top} que você colocou não tem o tanto escola para ele.Só tem {len(escolas_rede)} escolas.')
        return top_n_por_estado_e_rede(colecao)
       
    print(f'------TOP {top} DE {estado} DA REDE {rede.upper()}------')

    for i in range (0, top, 1):
        escola = escolas_rede[i]
        print(f'{i+1}° - {escola['nome']} - {escola['media_objetivas']}')
    
        
def media_nacional_por_area(colecao, area):
    somatorio = 0 

    if area == 1:

        for escola in colecao:
            somatorio += float(escola['linguagens'])

        print(f'A média Nacional pela área de Linguagens é de {(somatorio/len(colecao)):.2f} ')
       
    elif area == 2:
        for escola in colecao:
            somatorio += float(escola['matematica'])

        print(f'A média Nacional pela área de Matemática é de {(somatorio/len(colecao)):.2f} ')

    elif area == 3:
        for escola in colecao:
            somatorio += float(escola['ciencias_natureza'])

        print(f'A média Nacional pela área Ciências da Natureza é de {(somatorio/len(colecao)):.2f} ')

    elif area == 4:
        for escola in colecao:
            somatorio += float(escola['humanas'])

        print(f'A média Nacional pela área Ciências Humanas é de {(somatorio/len(colecao)):.2f} ')
        

    elif area == 5:
        for escola in colecao:
                somatorio += float(escola['redacao'])

        print(f'A média Nacional de Redação é de {(somatorio/len(colecao)):.2f} ')


def melhor_escola_por_area_estado_ou_br(colecao, area):


    if area == 1:

        menu = '''------ESTADO OU NACIONAL------
        1 - Estadual
        2 - Nacional

        >>> '''

        escolha = u.obter_numero_da_faixa(menu, 1, 2)
        
        if escolha == 1:
            estado = input('Estado(Ex: PI): ').upper()

            escolas_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
            escolas_ordenas = sorted(escolas_do_estado, key=lambda item: item['linguagens'], reverse=True)
            
            melhor_escola = escolas_ordenas[0]

            print(f'A melhor escola do Estado do {estado} na área de Linguagens:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['linguagens']} - Média objetiva {melhor_escola['media_objetivas']}')
       
        else:
            escola_ordenadas = sorted(colecao, key=lambda item: item['linguagens'], reverse=True)
            melhor_escola = escola_ordenadas[0]

            print('A melhor escola a nível Nacional foi na área de Linguagens:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['linguagens']} - Média objetiva {melhor_escola['media_objetivas']}')
        
        
       
    elif area == 2:
        menu = '''------ESTADO OU NACIONAL------
        1 - Estadual
        2 - Nacional

        >>> '''

        escolha = u.obter_numero_da_faixa(menu, 1, 2)
        
        if escolha == 1:
            estado = input('Estado(Ex: PI): ').upper()

            escolas_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
            escolas_ordenas = sorted(escolas_do_estado, key=lambda item: item['matematica'], reverse=True)
            
            melhor_escola = escolas_ordenas[0]

            print(f'A melhor escola do Estado do {estado} na área de Matemática:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['matematica']} - Média objetiva {melhor_escola['media_objetivas']}')
       
        else:
            escola_ordenadas = sorted(colecao, key=lambda item: item['matematica'], reverse=True)
            melhor_escola = escola_ordenadas[0]

            print('A melhor escola a nível Nacional foi na área de Matemática:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['matematica']} - Média objetiva {melhor_escola['media_objetivas']}')

    elif area == 3:
        escolas_area = filtrar(colecao, lambda item: item['area'] == area)

        menu = '''------ESTADO OU NACIONAL------
        1 - Estadual
        2 - Nacional

        >>> '''

        escolha = u.obter_numero_da_faixa(menu, 1, 2)
        
        if escolha == 1:
            estado = input('Estado(Ex: PI): ').upper()

            escolas_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
            escolas_ordenas = sorted(escolas_do_estado, key=lambda item: item['ciencia_natureza'], reverse=True)
            
            melhor_escola = escolas_ordenas[0]

            print(f'A melhor escola do Estado do {estado} na área de Ciências da Natureza:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['ciencia_natureza']} - Média objetiva {melhor_escola['media_objetivas']}')
       
        else:
            escola_ordenadas = sorted(colecao, key=lambda item: item['ciencia_natureza'], reverse=True)
            melhor_escola = escola_ordenadas[0]

            print('A melhor escola a nível Nacional foi na área de Ciências da Natureza:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['ciencia_natureza']} - Média objetiva {melhor_escola['media_objetivas']}')
    
    elif area == 4:
        menu = '''------ESTADO OU NACIONAL------
        1 - Estadual
        2 - Nacional

        >>> '''

        escolha = u.obter_numero_da_faixa(menu, 1, 2)
        
        if escolha == 1:
            estado = input('Estado(Ex: PI): ').upper()

            escolas_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
            escolas_ordenas = sorted(escolas_do_estado, key=lambda item: item['humanas'], reverse=True)
            
            melhor_escola = escolas_ordenas[0]

            print(f'A melhor escola do Estado do {estado} na área de Ciências Humanas:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['humanas']} - Média objetiva {melhor_escola['media_objetivas']}')
       
        else:
            escola_ordenadas = sorted(colecao, key=lambda item: item['humanas'], reverse=True)
            melhor_escola = escola_ordenadas[0]

            print('A melhor escola a nível Nacional foi na área de Ciências Humanas:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['humanas']} - Média objetiva {melhor_escola['media_objetivas']}')
        

    elif area == 5:

        menu = '''------ESTADO OU NACIONAL------
            1 - Estadual
            2 - Nacional

            >>> '''

        escolha = u.obter_numero_da_faixa(menu, 1, 2)
        
        if escolha == 1:
            estado = input('Estado(Ex: PI): ').upper()

            escolas_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
            escolas_ordenas = sorted(escolas_do_estado, key=lambda item: item['redacao'], reverse=True)
            
            melhor_escola = escolas_ordenas[0]

            print(f'A melhor escola do Estado do {estado} na Redação:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['redacao']} - Média objetiva {melhor_escola['media_objetivas']}')
       
        else:
            escola_ordenadas = sorted(colecao, key=lambda item: item['redacao'], reverse=True)
            melhor_escola = escola_ordenadas[0]

            print('A melhor escola a nível Nacional foi na Redação:')
            print(f'{melhor_escola['nome']} - {melhor_escola['uf']} - {melhor_escola['redacao']} - Média objetiva {melhor_escola['media_objetivas']}')
    
        
def listar_escolas_por_estado_renda(colecao):
    estado = input('Estado(Ex: PI): ').upper()

    lista_ordenada = sorted(filtrar(colecao, lambda item: item['uf'] == estado), key=lambda item: item['nivel_socio_economico'], reverse=True)

    print(f'As Escolas do Estado de {estado} ordenadas por renda:\n')

    for i in range (0, len(lista_ordenada), 1):
        escola = lista_ordenada[i]
        print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['nivel_socio_economico']} - Média objetiva: {escola['media_objetivas']}')
        

def busca_especifica(colecao):
    parte = input('Parte do nome da escola que quer buscar: ').upper()
    i = 1

    for escola in colecao:
        nome = escola['nome']

        if parte in nome:
            print(f'{i}° - {escola['nome']} - Média objetiva {escola['media_objetivas']} - Estados: {escola['uf']} -  Município: {escola['municipio']}')
            i += 1


def ranking_por_estado(colecao):
    estado = input('Estado(Ex: PI): ').upper()

    lista_do_estado = filtrar(colecao, lambda item: item['uf'] == estado)
    lista_ordenada = sorted(lista_do_estado, key=lambda item: item['media_objetivas'], reverse=True)

    print(f'---------RANKING ENEM 2014 NO ESTADO DO {estado}---------\n')

    for i in range(0, len(lista_ordenada), 1):
        escola = lista_ordenada[i]

        print(f'{i+1}° - {escola['nome']} - {escola['rede']} - {escola['media_objetivas']} - {escola['municipio']}')