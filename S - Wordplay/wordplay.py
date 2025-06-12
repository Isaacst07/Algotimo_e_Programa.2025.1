import utils


def main():
    utils.limpar_tela()
    
    menu = '''----------MENU----------
1 - Palavras sem a letra desejada
2 - Palavras com o tamanho N

0 - Sair
'''

    while True:
        print(menu)
        opcao = utils.obter_numero_entre_int('Qual sua opção(1/2/0): ', 0, 2)

        if opcao == 0:
            break

        if opcao == 1:
            arquivo = open('word.txt')
            letra = utils.obter_string('Qual o caractere não desejado >>> ')
            has_no_caractere(letra, arquivo)
        elif opcao ==2:
            arquivo = open('word.txt')
            tamanho = utils.obter_numero_inteiro('Qual o tanto de carcteres a palavra deve ter: ')
            verificar_tamanho(tamanho, arquivo)

        input('Enter to continue...')
        utils.limpar_tela()

    print('Fim.')
        


def verificar_tamanho(tamanho: int, arquivo):
    contador = 0
    contador_filtro = 0
    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if len(palavra) >= tamanho:
            print(palavra)
            contador_filtro += 1

    percentual = (contador_filtro / contador) * 1000
    print(f'Percentual de palavras de tamanho {tamanho}: {contador_filtro}/{contador} - ({percentual:.2f}%)')


def has_no_caractere(caractere :str, arquivo):
    contador = 0 
    contador_filtro = 0
    for linha in arquivo:
        contador += 1
        palavra = linha.strip()
        if caractere.strip() not in palavra:
            contador_filtro += 1
            print(linha)

    percentual = (contador_filtro / contador) * 100
    print(f'Percentual de palavras sem o a letra "{caractere}": {contador_filtro}/{contador} - ({percentual:.2f}%)')


main()