def main():
    primos = gerar_primos(3500) 
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            sobrevivente = josephus_variavel(n, primos)
            print(sobrevivente)
        except EOFError:
            break

        
def gerar_primos(limite):
    primos = []
    num = 2
    while len(primos) < limite:
        for p in primos:
            if num % p == 0:
                break
        else:
            primos.append(num)
        num += 1
    return primos

def josephus_variavel(n, primos):
    pessoas = list(range(1, n + 1))  
    idx = 0  
    for i in range(n - 1):  
        m = primos[i]  
        idx = (idx + m - 1) % len(pessoas)  
        pessoas.pop(idx)  
    return pessoas[0]  


main()
