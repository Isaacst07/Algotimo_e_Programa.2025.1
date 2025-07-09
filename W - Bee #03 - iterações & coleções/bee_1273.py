def main():
    primeiro_caso = True  
    
    while True:
        palavras = []
        n = int(input())
        
        if n == 0:
            break

        for i in range(n):
            palavra = input()
            palavras.append(palavra)

        maior_palavra = maior(palavras)

        if not primeiro_caso:
            print() 
        else:
            primeiro_caso = False

        for palavra in palavras:
            diferenca = maior_palavra - len(palavra)
            palavra_alinhada = ' ' * diferenca + palavra
            print(palavra_alinhada)


def maior(lista):
    maior = 0

    for i in range(len(lista)):
        if len(lista[i]) > maior:
            maior = len(lista[i])

    return maior


main()
