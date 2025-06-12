# Entrada 

m = int (input ('Quantos minutos: '))

# Processamento 

dias = m // 1440
horas = (m % 1440) // 60
minutos = m - (dias * 1440) - (horas * 60)

# Saída 

print (f'{m} minutos equivalem a {dias} dias, {horas} horas e {minutos} minutos. ')