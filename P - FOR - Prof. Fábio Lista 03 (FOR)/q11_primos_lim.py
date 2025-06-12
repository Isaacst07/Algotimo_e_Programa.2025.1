import utils


def main():
    lim_inf = utils.obter_numero_inteiro('Limite Inferior: ')
    lim_sup = utils.obter_numero_min_int('Limite Superior: ', lim_inf+1)

    for i in range (lim_inf, lim_sup+1, 1):
        if eh_primo(i) == True:
            print(i)

    print('FIM!')


def eh_primo(numero: int):
    divisores = 1
    candidato = 2 

    for i in range(candidato, numero+1, 1):
        if numero % i == 0:
            divisores += 1

    if numero == 1:
        return False
    elif divisores == 2:
        return True
    else:
        return False


main()