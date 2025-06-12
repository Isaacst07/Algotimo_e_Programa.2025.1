from funcoes import obter_numero_inteiro

def main():
    a = obter_numero_inteiro('Escreva o primeiro termo da P.A: ')
    razao_r = obter_numero_inteiro('Escreva a razão da P.A: ' )
    limite = validar_limite(a, razao_r)

    print(f'Os termos da P.A menor que o limite {limite} são iguais a: ')
    ler_menores_limites(a, razao_r, limite)


def validar_limite(a: int, razao: int) -> int:
    while True:
        limite = obter_numero_inteiro('Digite o limite para os termos da P.A: ')

        if razao > 0 and a < limite:
            return limite
        elif razao < 0 and a > limite:
            return limite
        elif razao == 0 and a < limite:
            return limite
        else:
            print("Com esses valores, nenhum termo da P.A será menor que o limite. Tente novamente.")


def ler_menores_limites(a, razao_r, limite):
    if razao_r == 0:
        if a < limite:
            print(a)
    else:    
     progressao = a
     while progressao < limite if razao_r > 0 else progressao > limite:
            print(a)
            progressao += razao_r
            print(progressao)
           

main()