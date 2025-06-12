import funcoes

def main():
    fichas = funcoes.obter_numero_inteiro('Quantas fichas você quer depositar: ')
    funcoes.limpar_tela()
    controle_fichas(fichas)


def controle_fichas(fichas: int):
    contador = 1
    nome_maior = ''
    peso_maior = None
    nome_menor = ''
    peso_menor = None  

    while contador <= fichas:
        print(F'------------FICHA DO BOI {contador}------------')
        nome = str(input('Nome do boi: '))
        peso = funcoes.obter_numero_real('Peso do boi(kg): ')

        if peso_maior == None or peso > peso_maior:
            peso_maior = peso
            nome_maior = nome
        
        if peso_menor == None or peso < peso_menor:
            peso_menor = peso
            nome_menor = nome

        funcoes.limpar_tela()
        contador += 1 

    print(f'''
--------RELATÓRIO DAS FICHAS--------
O nome do boi mais pesado é: {nome_maior}
E seu peso é: {peso_maior} kg
Já o nome do boi menos pesado é: {nome_menor}
E seu peso é: {peso_menor} kg
          
          ''')


main()