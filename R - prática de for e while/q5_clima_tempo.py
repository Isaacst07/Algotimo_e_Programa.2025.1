import os


def main():
    limpar_tela()

    print('Olá, vamos monitorar o clima para você!')
    dar_espaco()

    qtd_horas = obter_numero_int('Quantidade de horas a se monitorar(h): ')
    limite_temperatura = obter_numero_float('Qual o limite de temperatura(C°): ')

    limpar_tela()

    maior_temperatura = 0 
    hora_maior_temperatura = 0 
    menor_umidade = 0
    hora_menor_umidade = 0
    qtd_execedeu_temp = 0
    
    for i in range (1, qtd_horas + 1, 1):
        limpar_tela()
        print(f'-----------{i}° hora-----------')
        temperatura = obter_numero_float(f'Temperatura(C°): ')
        umidade = obter_numero_float(f'Umidade(%): ')
        dar_espaco()
        print(f'Computamos o valor da {i}° hora, pressione enter para a próxima hora!')

        dar_espaco()

        input('Enter to continue ...')

        limpar_tela()

        if maior_temperatura == 0 or temperatura > maior_temperatura:
            maior_temperatura = temperatura
            hora_maior_temperatura = i

        if menor_umidade == 0 or umidade < menor_umidade:
            menor_umidade = umidade
            hora_menor_umidade = i

        if temperatura > limite_temperatura:
            qtd_execedeu_temp += 1

        
    print(f'''-----------RESUMO DO MONITORAMENTO DA TEMPERATURA-----------
a) A maior temperatura registrada: {maior_temperatura:.1f}C°, na {hora_maior_temperatura}° hora
b) A menor umidade resgistrada: {menor_umidade:.1f}%, na {hora_menor_umidade}° hora
c) Quantidade de vezes que a temperatura execedeu o limite: {qtd_execedeu_temp} 

''')


def obter_numero_float(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        return numero 
    except ValueError:
        print(f'O número "{entrada}" não é valido!')
        obter_numero_float(label)


def obter_numero_int(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
        return numero 
    except ValueError:
        print(f'O número "{entrada}" não é um interio valido!')
        obter_numero_int(label)


def dar_espaco():
    print('')


def limpar_tela():
    os.system('cls')


main()