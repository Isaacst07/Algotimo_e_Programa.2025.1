import utils 


def main():
    utils.limpar_tela()
    total_sim = 0 

    print('a)Você telefonou para a vítima? ')
    utils.dar_espaco()
    resposta1 = input('Resposta(S - Sim e N - Não): ')
    utils.limpar_tela()
    if resposta1.upper() == 'S':
        total_sim += 1

    print('b)Você esteve no local do crime? ')
    utils.dar_espaco()
    resposta2 = input('Resposta(S - Sim e N - Não): ')
    utils.limpar_tela()
    if resposta2.upper() == 'S':
        total_sim += 1

    print('c)Você mora perto da vítima? ')
    utils.dar_espaco()
    resposta3 = input('Resposta(S - Sim e N - Não): ')
    utils.limpar_tela()
    if resposta3.upper() == 'S':
        total_sim += 1

    print('d)Você devia para a vítima? ')
    utils.dar_espaco()
    resposta3 = input('Resposta(S - Sim e N - Não): ')
    utils.limpar_tela()
    if resposta1.upper() == 'S':
        total_sim += 1

    print('e)Já trabalhou com a vítima? ')
    utils.dar_espaco()
    resposta3 = input('Resposta(S - Sim e N - Não): ')
    utils.limpar_tela()
    if resposta1.upper() == 'S':
        total_sim += 1


    print('Ápos o questionário você é ...')
    utils.esperar(2000)
    print(participacao_crime(total_sim))


def participacao_crime(resposta: int):
    if resposta == 5:
        return f'ASSASSINO !'
    elif resposta == 3 or resposta == 4:
        return f'CÚMPLICE !'
    elif resposta == 2:
        return f'SUSPEITO !'
    else:
        return f'INOCENTE !'
    

main()