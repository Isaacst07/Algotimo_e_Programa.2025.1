# Entrada 

anos_que_fuma = int (input ('Há quantos anos você fuma: '))
cigarros_dias = int (input ('Quantos cigarros você fuma por dia: '))
preço_da_carteira = float (input ('Preço da carteira de ciegarro: '))

# Processamento

carteiras = (365 * anos_que_fuma * cigarros_dias) /20
gasto = carteiras * preço_da_carteira

# Saída

print (f'Você gastou ao longo desses {anos_que_fuma} anos {gasto:.2f}R$. ')