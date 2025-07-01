def main():
    a , b = map(int, (input()).split())

    sao_primos(a, b)


def sao_primos(a: int, b: int):
    if a % b == 0 or b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

    
main()