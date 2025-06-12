import utils


def main():
    utils.limpar_tela()
    
    print('Olá, vamos calcular a folha de pagamento para você!')

    utils.dar_espaco()

    valor_hora = utils.obter_numero_real('Valor da hora trabalhada(R$): ')
    qtd_hora = utils.obter_numero_inteiro('Horas trabalhadas(H): ')

    utils.limpar_tela()

    print(calcular_folha_pagamento(valor_hora, qtd_hora))


def calcular_folha_pagamento(valor_hora: float, quantidade_horas: int):
    salario_bruto = valor_hora * quantidade_horas

    if salario_bruto <= 900:
        ir = 0 
        inss = salario_bruto * 0.1
        fgts = salario_bruto * 0.11
        total_desconto = ir + inss
        salario_liquido = salario_bruto - total_desconto

        folha = f'''---------------FOLHA DE PAGAMENTO---------------
Salário Bruto: ({valor_hora} * {quantidade_horas})  :R$ {salario_bruto:.2f}
(-) IR (0%)                 :R$ {ir:.2f}
(-) INSS (10%)              :R$ {inss:.2f}
FGTS (11%)                  :R$ {fgts:.2f}
Total de descontos          :R$ {total_desconto:.2f}
Salário Líquido             :R$ {salario_liquido:.2f}
'''
        return folha 
    
    elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
        inss = salario_bruto * 0.1
        fgts = salario_bruto * 0.11
        total_desconto = ir + inss
        salario_liquido = salario_bruto - total_desconto

        folha = f'''---------------FOLHA DE PAGAMENTO---------------
Salário Bruto: ({valor_hora} * {quantidade_horas})  :R$ {salario_bruto:.2f}
(-) IR (0%)                 :R$ {ir:.2f}
(-) INSS (10%)              :R$ {inss:.2f}
FGTS (11%)                  :R$ {fgts:.2f}
Total de descontos          :R$ {total_desconto:.2f}
Salário Líquido             :R$ {salario_liquido:.2f}
'''
        return folha
    
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.1 
        inss = salario_bruto * 0.1
        fgts = salario_bruto * 0.11
        total_desconto = ir + inss
        salario_liquido = salario_bruto - total_desconto

        folha = f'''---------------FOLHA DE PAGAMENTO---------------
Salário Bruto: ({valor_hora} * {quantidade_horas})  :R$ {salario_bruto:.2f}
(-) IR (0%)                 :R$ {ir:.2f}
(-) INSS (10%)              :R$ {inss:.2f}
FGTS (11%)                  :R$ {fgts:.2f}
Total de descontos          :R$ {total_desconto:.2f}
Salário Líquido             :R$ {salario_liquido:.2f}
'''
        return folha
    
    else: 
        ir = salario_bruto * 0.2
        inss = salario_bruto * 0.1
        fgts = salario_bruto * 0.11
        total_desconto = ir + inss
        salario_liquido = salario_bruto - total_desconto

        folha = f'''---------------FOLHA DE PAGAMENTO---------------
Salário Bruto: ({valor_hora} * {quantidade_horas})  :R$ {salario_bruto:.2f}
(-) IR (0%)                 :R$ {ir:.2f}
(-) INSS (10%)              :R$ {inss:.2f}
FGTS (11%)                  :R$ {fgts:.2f}
Total de descontos          :R$ {total_desconto:.2f}
Salário Líquido             :R$ {salario_liquido:.2f}
'''
        return folha


main()