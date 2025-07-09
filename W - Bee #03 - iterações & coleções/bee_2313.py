def main():
    a, b, c = map(int, input().split())
    maior = eh_maior(a, b, c)
    medio = num_do_meio(a, b, c)
    menor = eh_menor(a, b, c)

    if a + b > c and a + c > b and b + c > a:

        if a == b and b == c:
            print('Valido-Equilatero')

        elif a != b and a != c and b != c:
            print('Valido-Escaleno')

        elif a == b or b == c or c == a:
            print('Valido-Isoceles')

        if (medio ** 2 + menor ** 2) == maior ** 2:
                print('Retangulo: S')
        else:
                print('Retangulo: N')

    else:
        print('Invalido')

def eh_maior(n1: int, n2: int, n3: int):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    

def num_do_meio(n1: int, n2: int, n3: int):
    if (n1 < n2 and n1 > n3) or (n1 < n3 and n1 > n2):
        return n1 
    elif (n2 < n1 and n2 > n3) or (n2 < n3 and n2 > n1):
        return n2
    else:
        return n3 
        

def eh_menor(n1: int, n2: int, n3: int):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3


main()