def main():
    a, b, c, d = map(int,(input()).split())

    resultado = valor_aceito(a,b,c,d)
    print(resultado)
    

def valor_aceito(a:int, b: int, c: int, d: int):
    if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
        return 'Valores aceitos'
    else:
        return 'Valores nao aceitos'


main()