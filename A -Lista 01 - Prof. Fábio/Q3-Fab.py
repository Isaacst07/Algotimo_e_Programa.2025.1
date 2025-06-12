# Entrada 

m = int (input('Minutos: '))


# Processamento

horas = m // 60
minutos = m - (horas * 60)

# Saída 

print (f'{m} minutos são {horas}h{minutos}min.')