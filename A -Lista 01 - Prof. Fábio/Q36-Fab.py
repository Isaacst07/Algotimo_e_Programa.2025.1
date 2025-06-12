# Entrada 

anos = int (input ('Quantos anos de idade: '))
meses = int (input ('E quantos meses de idade: '))
dias = int (input ('E quantos dias de idade:  '))

# Processamento

dias_de_vida = (anos * 365) + (meses * 30) + dias

# Saída

print (f'Com {anos} anos, {meses} meses e {dias} dias você tem {dias_de_vida} dias de vida. ')
