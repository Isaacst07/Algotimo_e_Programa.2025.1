def main():
    contador = 0
    soma_notas = 0

    while contador < 2:
        nota = float(input())

        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            contador += 1
            soma_notas += nota

    media = soma_notas / 2

    print(f'media = {media:.2f}')
    


main()