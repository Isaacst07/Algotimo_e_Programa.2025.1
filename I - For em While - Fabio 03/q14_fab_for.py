from funcoes import obter_numero_inteiro

def main():
    n = obter_numero_inteiro('Digite um número: ')
    candidato = 1
    quadrado = 1 

    while (candidato ** 2) <= n:
        quadrado = candidato ** 2
        candidato += 1 

    print(f'O maior quadrado perfeio menor ou igual a {n} é {quadrado} (sendo o quadrado de {quadrado ** 0.5})')


main()