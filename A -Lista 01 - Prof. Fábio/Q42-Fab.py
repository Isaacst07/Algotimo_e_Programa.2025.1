# Entrada 

x1 = int (input ('Ponto x1: '))
y1 = int (input ('Ponto y1: '))
x2 = int (input ('Ponto x2: '))
y2 = int (input ('Ponto y2: '))

# Processamento

parte_1 = (x2 - x1) ** 2
parte_2 = (y2 - y1) ** 2
d = (parte_1 + parte_2) ** (1/2)

# Saída

print (f'O resultado de D será: {d} . ')