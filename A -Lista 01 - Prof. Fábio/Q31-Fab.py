# Entrada 

numero = int (input ('Número binário de 4 digítos: '))

# Processamento 

m = numero // 1000
c = (numero % 1000) // 100
d = ((numero % 1000) % 100) // 10
u = (((numero % 1000) % 100) % 10) / 1
parte_4 = u * (2 ** 0)
parte_3 = d * (2 ** 1)
parte_2 = c * (2 ** 2)
parte_1 = m * (2 ** 3)
decimal = parte_1 + parte_2 + parte_3 + parte_4

# Saída 

print (f'O número binário {numero} na base decimal é {decimal:.0f} . ')