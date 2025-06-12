import os


def main():
    limpar_tela()
    print('Olá, vamos ajudar você a calcular a variação de temperatura!')
    dar_espaco()

    qtd_anos = obter_numero_int('Quantidade de anos que vamos analisar: ')
    metade_ano = qtd_anos // 2
    primeira_metade = 0
    segunda_metade = 0
    maior_temperatura = 0
    ano_maior_temperatura = 0 
    menor_temperatura = 0 
    ano_menor_temperatura = 0
     

    for i in range (1, qtd_anos + 1, 1):
        limpar_tela()
        print(f'------{i}° ANO------')
        media_temperatura = obter_numero_float('Média de temperatura do ano(C°): ')

        if i <= metade_ano:
            primeira_metade += media_temperatura
        else:
            segunda_metade += media_temperatura

        if maior_temperatura == 0 or media_temperatura > maior_temperatura:
            maior_temperatura = media_temperatura
            ano_maior_temperatura = i 

        if menor_temperatura == 0 or media_temperatura < menor_temperatura:
            menor_temperatura = media_temperatura
            ano_menor_temperatura = i

    limpar_tela()
    tendencia = tendencia_de_melhorar(primeira_metade, segunda_metade, metade_ano)

    print(f'''------TENDÊNCIA DE TEMPERATURA MÁXIMA------
a) Ano com maior temperatura: {ano_maior_temperatura}° com {maior_temperatura}C°
b) Ano com menor temperatura: {ano_menor_temperatura}° com {menor_temperatura}C°
c) Média geral das temperaturas: {(primeira_metade + segunda_metade)/ qtd_anos:.2f} C°
{tendencia}

''')
    

def tendencia_de_melhorar(primeira_metade: float, segunda_metade: float, metade: int):
    media_primeira_metade = primeira_metade / metade
    media_segunda_metade = segunda_metade / (metade + 1)

    if media_primeira_metade > media_segunda_metade:
        return f'Não houve melhora significativa na média das temperaturas!'
    elif media_primeira_metade == media_segunda_metade:
        return f'A tendência foi a mesma do início ao fim do período!'
    else:
        return f'Tendência de melhora observada na média das temperaturas!'


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