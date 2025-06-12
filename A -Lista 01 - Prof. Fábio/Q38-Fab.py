# Entrada 

n1 = int (input ('Numerador da primeira fração: '))
d1 = int (input ('Denominador da primeira fração: '))
n2 = int ( input ('Numerador da segunda fração: '))
d2 = int (input ('Denominador da segunda fração: '))

# Processamento

denominador = d1 * d2 
numerador = (n1 * d2) + (d1 * n2)


# Saída

print (f'A soma das frações: {n1} / {d1} + {n2} / {d2} = {numerador:.0f} / {denominador:.0f} . ')