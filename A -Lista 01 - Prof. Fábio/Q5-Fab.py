# Entrada 

numero = int (input ('Número: ' ))

# Processamento

c = numero // 100
d = (numero % 100) // 10 
u = (numero % 10)  / 1 
soma = c + d + u 

# Saída

print  (f'A soma dos elementos do número {numero} é {soma}.')