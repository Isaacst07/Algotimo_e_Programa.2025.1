# Entrada 

numero = int (input ('Número de 3 digítos: '))

# Processamento

c = numero // 100
d = (numero % 100) // 10
u = (numero % 10) % 10
 

# Saída 

print (f'O inverso do número {numero} é {u:.0f}{d}{c}. ')