import os

alimentos = {'frango': {'calorias': 165, 'proteina': 31}, 'arroz':{'calorias': 130, 'proteina':2.7}, 'ovo': {'calorias': 77, 'proteina': 6.3}, 
                 'feijao': {'calorias': 132, 'proteina': 12}, 'farinha': {'calorias': 14, 'proteina': 6.9}
                 }


def main():
    limpar_tela()

    qtd_pessoas = obter_numero_int_min('Quantidade de pessoas: ', 0)

    menor_consumo = 0
    menor_pessoa = 0
    maior_consumo = 0
    maior_pessoa = 0
    total_calorias = 0
    total_proteinas = 0

    for pessoa in range (1, qtd_pessoas + 1, 1):
        print(f'-------{pessoa}° PESSOA-------')
        qtd_produtos = obter_numero_int_min('Quantidade de produtos: ',0)

        for produto in range (1, qtd_produtos + 1, 1):
            produto = alimento_na_lista()
            gramas = obter_numero_float_min('Peso do alimento(g): ',0)

            calorias = (alimentos[produto]['calorias'] * gramas) / 100
            proteinas = (alimentos[produto]['proteinas'] * gramas) / 100

            total_calorias += calorias
            total_proteinas += proteinas

            if maior_consumo == 0 or calorias > maior_consumo:
                maior_consumo = calorias
                maior_pessoa = pessoa

            if menor_consumo == 0 or calorias < menor_consumo:
                menor_consumo = calorias
                menor_pessoa = pessoa 

            print(f'''-----CONSUMO DA {pessoa}° PESSOA-----
a) Consumo calórico: {calorias:.2f} calorias
b) Consumo proteico: {proteinas:.2f} gramas de proteina          
''')
    
    limpar_tela()
    print(f'''
a) A pessoa com maior consumo: {maior_consumo} calorias, foi a {maior_pessoa}° pessoa
b) A pessoa com menor consumo: {menor_consumo} calorias, foi a {menor_pessoa}° pessoa
''')

    print('Fim.')
        

def alimento_na_lista():
    while True:
        produto = str(input('Qual o produto: '))

        if produto in alimentos:
            return produto
        else:
            print(f'O alimento {produto}.Não está na lista de alimentos.')
            alimento_na_lista()


def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um interio válido!')
        obter_numero_int(label)


def obter_numero_int_min(label: str, min: int):
    numero = obter_numero_int(label)

    if numero >= min:
        return numero
    else:
        print(f'O valor "{numero}" é menor que o minímo {min}!')
        obter_numero_int_min(label)


def obter_numero_int_min_max(label: str, min: int, max: int):
    numero = obter_numero_int(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'O valor "{numero}" não está entre o limite minímo {min} e o limite máximo {max}!')
        obter_numero_int_min_max(label)
    

def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f'O número "{entrada}" não é um numero válido!')
        obter_numero_float(label)


def obter_numero_float_min(label: str, min: int):
    numero = obter_numero_float(label)

    if numero >= min:
        return numero
    else:
        print(f'O valor "{numero}" é menor que o minímo {min}!')
        obter_numero_float_min(label)


def obter_numero_float_min_max(label: str, min: int, max: int):
    numero = obter_numero_float(label)

    if numero >= min and numero <= max:
        return numero
    else:
        print(f'O valor "{numero}" não está entre o limite minímo {min} e o limite máximo {max}!')
        obter_numero_float_min_max(label)


def limpar_tela():
    os.system('cls')


def dar_espaco():
    print('')


main()