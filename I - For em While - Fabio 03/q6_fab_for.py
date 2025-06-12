def main(): 

    tabuada_inicial = 1
    while tabuada_inicial <= 10:
        print(f'----- TABUADA DO {tabuada_inicial} ----- ')

        contador = 1
        while contador <= 10:
            resultado = tabuada_inicial * contador 
            print(f'{tabuada_inicial} X {contador} = {resultado}')
            contador += 1
             
        tabuada_inicial += 1  
        

main()
