# Entrada 

preco_inicial = float (input ('Preço inicial(R$): '))
percentual = int (input ('Percentual de desconto(%): '))

# Processamento

desconto = (preco_inicial / 100) * percentual
valor_final = preco_inicial - desconto

# Saída

print (f' Um bem de preço {preco_inicial:.2f}R$ ')
print (f' Com um desconto percentual {percentual}%')
print (f' Ficará no valor de {valor_final:.2f}R$ ')