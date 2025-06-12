import utils 


def main():
    utils.limpar_tela()

    dia = utils.obter_numero_inteiro('Digite um número: ')

    utils.limpar_tela()
    print('E o dia da semana é ...')

    utils.dar_espaco()

    utils.esperar(2000)
    print(qual_dia_eh(dia))


def qual_dia_eh(dia: int):

    if dia == 1:
        return 'É Domingo, IRU!'
    elif dia == 2:
        return 'É Segunda, IRU!'
    elif dia == 3:
        return 'É Terça, IRU!'
    elif dia == 4:
        return 'É Quarta, IRU!'
    elif dia == 5:
        return 'É Quinta, IRU!'
    elif dia == 6:
        return 'É Sexta, IRU!'
    elif dia == 7:
        return 'É Sábado, IRU!'
    else:
        return 'Inválido. Na próxima digita um dia certo né :('


main()