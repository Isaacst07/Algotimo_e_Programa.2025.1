# Entrada 

s = int (input ('Quantos segundos: '))

# Processamento 

horas  = s // 3600
minutos  = (s % 3600) // 60
segundos = s - (horas * 3600) - (minutos * 60)

# Saída 

print (f'{s} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos. ')