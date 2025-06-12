# Entrada 

a = int (input ('Coeficiente A: '))
b = int (input ('Coeficiente B: '))
c = int (input ('Coeficiente C: '))
d = int (input ('Coeficiente D: '))
e = int (input ('Coeficiente E: '))
f = int (input ('Coeficiente F: '))

# Processamento

x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

# Saída

print (f'Os valores respectivos de x e y são {x:.2f} e {y:.2f} .')
