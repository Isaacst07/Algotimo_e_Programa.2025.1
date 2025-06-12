# Entrada 

h = int (input ('Quantas horas: '))

# Processamento 

semanas = h // 168
dias = (h % 168) // 24
horas = h - (semanas * 168) - (dias * 24)


# Saída 

print (f'{h} horas equivale a {semanas} semanas,{dias} dias e {horas} horas. ')