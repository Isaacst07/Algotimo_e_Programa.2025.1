import utils


def main():
    letra = utils.obter_string('Digite uma letra: ')

    utils.limpar_tela()

    eh_consoante_ou_vogal(letra)


def eh_consoante_ou_vogal(letra: str):
    if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
        return print(f'A letra digitada "{letra}" é uma VOGAL!')
    else:
        return print(f'A letra digitada "{letra}" é uma CONSOANTE!')


main()