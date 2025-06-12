# Entrada 

valor = int (input ('valor que vai sacar(R$): '))

# Processamento

notas_50 = valor // 50
notas_10 = (valor % 50) // 10
notas_5 = ((valor % 50) % 10 ) // 5
notas_1 = (((valor % 50) % 10) % 5) // 1 

# Saída

print (f'Serão {notas_50} de 50R$, {notas_10} de 10R$, {notas_5} de 5R$ e {notas_1} de 1R$. ')