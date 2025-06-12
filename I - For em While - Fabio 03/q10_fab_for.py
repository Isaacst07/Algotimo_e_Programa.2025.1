from  funcoes import obter_numero_interio_min

def main():
    limite_inf = obter_numero_interio_min('Qual o limite inferior: ', 0)
    limite_sup = obter_numero_interio_min('Qual o limite superior: ', limite_inf + 1)

    eh_impar(limite_inf, limite_sup)

def eh_impar(limite_inf, limite_sup):
    candidato = limite_inf

    print(f'Os números ímpares entre o limite inferior {limite_inf} e limite superior {limite_sup}')

    while candidato <= limite_sup:
        if candidato % 2 != 0:
            print(f'{candidato}')
        candidato += 1 


main()