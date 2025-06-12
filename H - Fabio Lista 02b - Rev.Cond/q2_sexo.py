import utils


def main():
    sexo = utils.obter_string('Digite um sexo(M - Masculino ou F - Feminino): ')

    utils.limpar_tela()

    eh_masc_ou_fem(sexo)


def eh_masc_ou_fem(sexo: str):
    if sexo == 'M' or sexo == 'm':
        return print(f'O sexo digitado é Masculino!')
    elif sexo == 'F' or sexo =='f':
        return print(f'O sexo digitado é Feminino!')
    else:
        return print(f'O sexo digitado é INVÁLIDO!')
    

main()