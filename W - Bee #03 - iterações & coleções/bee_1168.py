def main():
    leds = {'1' : 2, '2' : 5, '3' : 5, '4' : 4, '5' : 5, '6' : 6, '7' : 3, '8' : 7, '9' : 6, '0' : 6 }
    n = int(input())

    for i in range (0, n, 1):
        valor = input()
        qtd_leds = 0

        for caracter in valor:
            leds_usados = leds[caracter]
            qtd_leds += leds_usados
        
        print(f'{qtd_leds} leds')


main()