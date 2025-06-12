# Entrada 

numero = int (input ('Número de 3 dígitos: '))

# Processamento 

c = numero // 100
d = (numero % 100) // 10
u = (numero % 10 )  % 10

inverso = (u * 100) + (d * 10) + c

soma = numero + inverso

# Saída 

print (f'A soma do número {numero} e seu inverso é {soma}. ')