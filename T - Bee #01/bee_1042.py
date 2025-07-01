def main():
    n1, n2, n3 = map(int, (input()).split())

    ordem_crescente(n1, n2, n3)
    print('')
    print(n1)
    print(n2)
    print(n3)


def ordem_crescente(n1: int, n2: int, n3: int):
    num_maior = eh_maior(n1, n2, n3)
    num_meio = num_do_meio(n1, n2, n3)
    num_menor = eh_menor(n1, n2, n3)
    
    print(num_menor)
    print(num_meio)
    print(num_maior)
    
    
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