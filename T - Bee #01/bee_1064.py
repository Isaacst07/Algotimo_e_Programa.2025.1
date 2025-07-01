def main():
    positivos = 0
    somatorio_positivos = 0
    
    n1 = float(input())
    if n1 > 0:
        positivos += 1
        somatorio_positivos += n1

    n2 = float(input())
    if n2 > 0:
        positivos += 1
        somatorio_positivos += n2

    n3 = float(input())
    if n3 > 0:
        positivos += 1
        somatorio_positivos += n3

    n4 = float(input())
    if n4 > 0:
        positivos += 1
        somatorio_positivos += n4

    n5 = float(input())
    if n5 > 0:
        positivos += 1
        somatorio_positivos += n5

    n6 = float(input())
    if n6 > 0:
        positivos += 1
        somatorio_positivos += n6

    media = somatorio_positivos / positivos
    
    print(f'{positivos} valores positivos\n{media:.1f}')
    

main()