# Entrada 

n1 = float (input ('Nota 1: '))
p1 = int (input ('Peso 1 : '))
n2 = float (input ('Nota 2: '))
p2 = int (input ('Peso 2: '))
n3 = float (input ('Nota 3: '))
p3= int (input ('Peso 3: '))

# Processamento 

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

# Saída 

print (f'A média pondera das notas é {media:.2f}. ')