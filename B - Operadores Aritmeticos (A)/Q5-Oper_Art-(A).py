valor = int (input ('valor que vai sacar(R$): '))

# Processamento

notas_50 = valor // 50
notas_10 = (valor % 50) // 10


# Saída

print (f'Serão {notas_50} de 50R$, {notas_10} de 10R$. ')