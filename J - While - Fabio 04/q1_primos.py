import utils


def main():
    qtd = utils.obter_numero_inteiro('Quantos números tem na lista: ')
    utils.limpar_tela()

    while qtd > 0:
        numero = utils.obter_numero_inteiro('Digite um número: ')

        if eh_primo(numero):
            print(f'O número {numero} é PRIMO!')
        else:
            print(f'O número {numero} NÃO É PRIMO!')
        
        qtd -= 1
    


def eh_primo(numero: int):
    if numero == 1: 
        return False
    
    candidato = 2 

    while candidato < 500 and candidato < numero:
        if numero % candidato == 0:
            return False
        candidato += 1 

    return True


main()