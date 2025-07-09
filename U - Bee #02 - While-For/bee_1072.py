def main():
    n = int(input())
    in_intervalo = 0
    

    for i in range(1, n + 1, 1):
        x = int(input())

        for y in range (10, 21, 1):
            if x == y:
                in_intervalo += 1

    out_intervalo = n - in_intervalo
    
    print(f'{in_intervalo} in\n{out_intervalo} out')


main()