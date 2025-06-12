import utils 


def main():
    n = utils.obter_numero_inteiro('N: ')
    quadrado = 0
    

    utils.limpar_tela()

    for i in range (1, n+1, 1):
        
        if (i ** 2) > n:    
            quadrado = (i - 1) ** 2
                
        if (i ** 2) == n:
            quadrado = i ** 2  
        
        if (i ** 2) >= n:
            break

    print(f'O maior quadrado perfeio menor ou igual a {n} é {quadrado} (sendo o quadrado de {(quadrado ** 0.5):.0f})')
 

main()