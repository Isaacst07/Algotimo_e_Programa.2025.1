from funcoes import obter_numero_interio_min

def main():
    limite_inf = obter_numero_interio_min('Qual o limite inferior: ', 0)
    limite_sup = obter_numero_interio_min('Qual limite superior: ', limite_inf + 1)

    eh_par(limite_inf, limite_sup)


def eh_par(limite_inf, limite_sup):
    candidato = limite_inf
    
    print(f'Os números pares entre {limite_inf} e {limite_sup}:')

    while candidato <= limite_sup:
        if candidato % 2 == 0:
            print(f'{candidato}')

        candidato += 1 
        

main()