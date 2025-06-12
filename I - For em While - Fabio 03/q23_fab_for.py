import funcoes

def main():
    ficha_func = funcoes.obter_numero_inteiro('Número de fichas: ')
    funcoes.limpar_tela()
    calcular_impostos(ficha_func)


def calcular_impostos(ficha_func=int):
    contador = 1 

    while contador <= ficha_func:

        codigo_func = funcoes.obter_numero_inteiro('Código do funcionário: ')
        horas_trab = funcoes.obter_numero_inteiro('Horas que trabalhadas pelo funcionário: ')
        num_depend = funcoes.obter_numero_inteiro('Número de dependentes (filhos): ')

        salario = (horas_trab * 12) + (40 * num_depend)
        desc_inss = salario * 0.085
        desc_ir = desc_inss * 0.05
        salario_liqui = salario - desc_inss - desc_ir

        funcoes.limpar_tela()

        print(F'-------------FUNCIONÁRIO {codigo_func}-------------')
        print(f'''
O salário do funcionário era: {salario:.2f} R$
Desconto INSS(8.5%): {desc_inss:.2f} R$
Desconto do Imposto de Renda(5%): {desc_ir:.2f} R$
O salário do funcionário líquido: {salario_liqui:.2f} R$
''')
        print('')
        print(input('Enter to continue ...'))
        funcoes.limpar_tela()
        
        contador += 1
     
    print('Fim por fim feito por mim !')


main()