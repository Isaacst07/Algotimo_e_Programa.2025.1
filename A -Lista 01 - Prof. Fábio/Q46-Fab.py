# Entrada 

valor_bem = float (input ('Valor do bem R$: '))

# Processamento

parcela = valor_bem // 3 
entrada = valor_bem - parcela - parcela 

# Saída

print ( f' A entrada será R$: {entrada:.2f}')
print (f'E as parcelas serão R$: {parcela:.2f}')
 