def main():
    par = []
    impar = []

    for i in range (0, 15, 1):
        valor = int(input())

        if valor % 2 == 0:
            par.append(valor)

            if len(par) == 5:
                for y in range(0, 5, 1):
                    print(f'par[{y}] = {par[y]}')
                par.clear()
        else:
            impar.append(valor)

            if len(impar) == 5:
                for y in range(0, 5, 1):
                    print(f'impar[{y}] = {impar[y]}')
                impar.clear()
        
    for j in range(0, len(impar), 1):
        print(f'impar[{j}] = {impar[j]}')
            
    for j in range(0, len(par), 1):
        print(f'par[{j}] = {par[j]}')
   

main()