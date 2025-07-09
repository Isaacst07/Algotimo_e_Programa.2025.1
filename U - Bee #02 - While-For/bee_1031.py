def main():
    while True:
        regioes = int(input())

        if regioes == 0:
            break

        salto = 1
        while True:
             
            if ultima_regiao(regioes, salto) == 13:
                print(salto)
                break

            salto += 1


def ultima_regiao(regioes, saltos):
    regioes_restantes = list(range(1, regioes + 1))
                
    regioes_restantes.pop(0) 
                
    indice_atual = 0 

    
    while len(regioes_restantes) > 1:
        
        indice_a_remover = (indice_atual + saltos - 1) % len(regioes_restantes)
                        
        regioes_restantes.pop(indice_a_remover)
                        
        indice_atual = indice_a_remover % len(regioes_restantes)

    return regioes_restantes[0]

main()