import utils 


def main():
    turno = utils.obter_string('Turno(M = Matutino, V = Vespertino e N = Noturno): ')

    utils.limpar_tela()

    print(f'{qual_turno(turno)}')


def qual_turno(turno: str):

    if turno.upper() == 'M':
        return 'Bom Dia!'
    elif turno.upper() == 'V':
        return 'Bom Tarde!'
    elif turno.upper() == 'M':
        return 'Boa Noite!'
    else:
        return 'Valor Inválido'


main()