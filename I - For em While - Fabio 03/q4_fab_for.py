from funcoes import obter_numero_inteiro
from funcoes import obter_numero_interio_min

def main():
    a = obter_numero_interio_min('Escreva o primeiro termo da P.G: ', 1)
    razao_r = obter_numero_inteiro('Escreva a razão da P.G: ')
    limite = obter_numero_inteiro('Escreva o limite que os termos podem atingir: ')
    print('Os termos da P.G são iguais a: ')
    ler_menores_limites(a, razao_r, limite)


def ler_menores_limites(a, razao_r, limite):
    progressao = (a * razao_r)
    print(a)
    while (progressao) < limite:
        print(progressao)
        (progressao) *= razao_r


main()