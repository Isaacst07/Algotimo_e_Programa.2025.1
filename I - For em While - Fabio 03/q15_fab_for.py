from funcoes import obter_numero_inteiro


def main():
    n = obter_numero_inteiro('Digíte um número: ')
    num_sequencia = 1
    somatorio = 2 

    print(f'Os n primeiros termos sequenciais:')
    print(f'{num_sequencia}')

    while num_sequencia < n:
        num_sequencia += somatorio
        print(f'{num_sequencia}')
        somatorio += 1 


main()