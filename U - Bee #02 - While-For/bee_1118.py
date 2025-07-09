def main():
    while True:
        nota1 = ler_nota()
        nota2 = ler_nota()
        media = (nota1 + nota2) / 2
        print(f"media = {media:.2f}")

        x = numero_em_faixa()

        if x == 2:
            break


def ler_nota():
    while True:
        nota = float(input())

        if 0 <= nota <= 10:
            return nota
        else:
            print('nota invalida')
        
            
def numero_em_faixa():
    while True:
        print('novo calculo (1-sim 2-nao)')
        
        opcao = int(input())

        if opcao == 1 or opcao == 2:
            break
        else:
            continue

    return opcao


main()
