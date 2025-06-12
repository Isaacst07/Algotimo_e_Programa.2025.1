import os


def main():
    limpar_tela()
    print('Olá, vamos monitorar seu treino para você!')
    dar_espaco()

    qtd_treinos = obter_numero_int('Quantidade de sessões de treino: ')
    maior_volume = 0
    treino_maior = 0 
    metade_treino = qtd_treinos // 2
    primeira_metade = 0
    segunda_metade = 0 
    
    for i in range (1, qtd_treinos + 1, 1):
        limpar_tela()

        print(f'--------{i}° SESSÃO DE TREINO--------')
        peso = obter_numero_float('Peso ultilizado nesse treino(Kg): ')
        repeticao = obter_numero_int('Quantidade de repetições: ')
        volume_total = peso * repeticao

        dar_espaco()
        print(f'O volume total dessa sessão foi de {volume_total}, de enter para continuar para a próxima sessão!')
        input('Enter to continue...')


        if maior_volume == 0 or volume_total > maior_volume:
            maior_volume = volume_total
            treino_maior = i

        if i <= metade_treino:
            primeira_metade += volume_total
        else:
            segunda_metade += volume_total
    
    limpar_tela()
    tendencia = tendencia_de_melhorar(primeira_metade, segunda_metade, metade_treino)

    print(f'''----------RESUMO DO TREINO----------
a) Sessão com maior volume: {treino_maior}° sessão com {maior_volume:.2f} de volume.
{tendencia}
''')
            

def tendencia_de_melhorar(primeira_metade: float, segunda_metade: float, metade: int):
    media_primeira_metade = primeira_metade / metade
    media_segunda_metade = segunda_metade / (metade + 1)

    if media_primeira_metade > media_segunda_metade:
        return f'Não houve melhora significativa!'
    elif media_primeira_metade == media_segunda_metade:
        return f'Você teve a mesma tendência do início ao final do treino!'
    else:
        return f'Tendência de melhora observada'


def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{numero}" não é um inteiro válido!')
        obter_numero_int(label)

    
def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número "{numero}" não é válido!')
        obter_numero_float(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()