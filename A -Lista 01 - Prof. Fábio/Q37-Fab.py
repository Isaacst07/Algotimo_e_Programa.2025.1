# Entrada 

d = int (input ('Sua idade em dias: '))

# Processamento

anos = d // 365
meses = (d % 365) // 30
dias = (d % 365) % 30

# Saída

print (f'Com {d} dias de vida você tem {anos} anos, {meses} meses e {dias} dias. ')
