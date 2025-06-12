import utils


def main():
    print('Olá,vou calcular o aumento dos colaboradores para você!')

    utils.dar_espaco()

    salario = utils.obter_numero_real('Salário do colaborador(R$): ')

    utils.limpar_tela()

    print(calcular_reajuste(salario))



def calcular_reajuste(salario: float):

    if salario <= 280:
        aumento = salario * 0.2
        salario_novo = salario + aumento
        resumo = f''''------------RESUMO DO AUMENTO------------
a) O salário antes do reajuste era: R$ {salario:.2f}
b) O percentual de aumento aplicado foi de: 20%
c) O valor do aumento foi de: R$ {aumento:.2f}
d) O novo salário, ápos o aumento é: R$ {salario_novo:.2f}  
        '''
        return resumo
    
    elif salario <= 700:
        aumento = salario * 0.15
        salario_novo = salario + aumento
        resumo = f''''------------RESUMO DO AUMENTO------------
a) O seu salário antes do reajuste era: R$ {salario:.2f}
b) O percentual de aumento aplicado foi de: 15%
c) O valor do aumento foi de: R$ {aumento:.2f}
d) O novo salário, ápos o aumento é: R$ {salario_novo:.2f}  
        '''
        return resumo
    
    elif salario <= 1500:
        aumento = salario * 0.1
        salario_novo = salario + aumento
        resumo = f''''------------RESUMO DO AUMENTO------------
a) O salário antes do reajuste era: R$ {salario:.2f}
b) O percentual de aumento aplicado foi de: 10%
c) O valor do aumento foi de: R$ {aumento:.2f}
d) O novo salário, ápos o aumento é: R$ {salario_novo:.2f}  
        '''
        return resumo
    
    else:
        aumento = salario * 0.05
    salario_novo = salario + aumento
    resumo = f''''------------RESUMO DO AUMENTO------------
a) O salário antes do reajuste era: R$ {salario:.2f}
b) O percentual de aumento aplicado foi de: 5%
c) O valor do aumento foi de: R$ {aumento:.2f}
d) O novo salário, ápos o aumento é: R$ {salario_novo:.2f}  
        '''
    return resumo


main()