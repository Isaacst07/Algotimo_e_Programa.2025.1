import utils


def main():
    print('------>PROMOÇÃO DE CARNES HIPERMERCADO TABAJARA<------')

    print('         Até 5 Kg      Acima de 5 Kg')
    print('File     R$ 4,90|    Kg R$ 5,80 por Kg')
    print('Alcatra  R$ 5,90|    Kg R$ 6,80 por Kg')
    print('Picanha  R$ 6,90|    Kg R$ 7,80 por Kg')

    tipo_carne = str(input('Carne comprada (F - File, A - Alcatra e P - Picanha): '))
    quilos = utils.obter_numero_real('Quantos Quilos(Kg): ')
    forma_de_pagamento = str(input('Forma de pagamento(C - Cartão Tabajara ou A - A vista): '))

    if tipo_carne.upper() == 'F' or tipo_carne.upper() == 'FILE':
        print(calcular_file(quilos, forma_de_pagamento))
    elif tipo_carne.upper() == 'A' or tipo_carne.upper() == 'ALCATRA' :
        print(calcular_alcatra(quilos, forma_de_pagamento))
    else:
        print(calcular_picanha(quilos, forma_de_pagamento))

    
def calcular_file(quilos: float, forma_de_pagamento: str):
     
    if forma_de_pagamento.upper() == 'C' or forma_de_pagamento.upper() == 'CARTAO TABAJARA' or forma_de_pagamento.upper() == 'CARTÃO TABAJARA':
        if quilos <= 5:
            preco_total = quilos * 4.90
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 5.80
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
    else:
        if quilos <= 5:
            preco_total = quilos * 4.90
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 5.80
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        

def calcular_alcatra(quilos: float, forma_de_pagamento: str):
     
    if forma_de_pagamento.upper() == 'C' or forma_de_pagamento.upper() == 'CARTAO TABAJARA' or forma_de_pagamento.upper() == 'CARTÃO TABAJARA':
        if quilos <= 5:
            preco_total = quilos * 5.90
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 6.80
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
    else:
        if quilos <= 5:
            preco_total = quilos * 5.90
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 6.80
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        

def calcular_picanha(quilos: float, forma_de_pagamento: str):
     
    if forma_de_pagamento.upper() == 'C' or forma_de_pagamento.upper() == 'CARTAO TABAJARA' or forma_de_pagamento.upper() == 'CARTÃO TABAJARA':
        if quilos <= 5:
            preco_total = quilos * 6.90
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 7.80
            desconto = preco_total * 0.05
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
    else:
        if quilos <= 5:
            preco_total = quilos * 6.90
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal
        
        else:
            preco_total = quilos * 7.80
            desconto = 0
            cupom_fiscal = f'''------------CUMPOM FISCAL------------
a) Tipo de carne: File
b) Quantidade de carne(Kg): {quilos:.2f} Kg
c) Preço total: R$ {preco_total:.2f}
d) Tipo de pagamento: Cartão Tabajara
e) Valor do desconto: R$ {desconto:.2f}
f) Valor a pagar: R$ {(preco_total - desconto):.2f}

'''     
            return cupom_fiscal


main()