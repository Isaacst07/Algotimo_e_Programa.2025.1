# Entrada 

numero = int (input ('Número de 3 dígitos: '))

# Processamento 

c = numero // 100
d = (numero % 100) // 10
u = (numero % 10 )  % 10

inverso = (u * 100) + (d * 10) + c

diferença = numero - inverso

# Saída 

print (f'A difereça entre o número {numero} e o seu inverso é {diferença}. ')