def main():
    number = float(input())

    resultado = intervalo_number(number)
    print(resultado)


def intervalo_number(number: float):
    if number >= 0 and number <= 25:
        return 'Intervalo [0,25]'
    elif number > 25 and number <= 50:
        return 'Intervalo (25,50]'
    elif number > 50 and number <= 70:
        return 'Intervalo (50,75]'
    elif number > 75 and number <= 100:
        return 'Intervalo (75,100]'
    else:
        return 'Fora de intervalo'
    

main()