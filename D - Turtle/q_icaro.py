def main():
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite um número inteiro maior que o anterior: '))
    candidato_num_impar = num1 

    print(f'Os números primos entre {num1} e {num2} são:')

    while candidato_num_impar <= num2:
        if eh_impar(candidato_num_impar) == True:
            print(f'{candidato_num_impar}')

        candidato_num_impar += 1


def eh_impar(numero):
    if numero % 2 != 0:
        return True
    

main()