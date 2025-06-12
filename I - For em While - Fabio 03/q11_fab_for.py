from funcoes import obter_numero_interio_min

def main():
    limite_inf = obter_numero_interio_min('Qual o limite inferior: ', 0)
    limite_sup = obter_numero_interio_min('Qual o limite superior: ', limite_inf + 1)

    print(f'Os primos entre o limite inferior {limite_inf} e limite superior {limite_sup}:')

    while limite_inf <= limite_sup:
        if eh_primo(limite_inf):
            print(f'{limite_inf}')
        limite_inf += 1


def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        i = 2
        while i * i <= numero:
            if numero % i == 0:
                return False
            i += 1
        return True


main()