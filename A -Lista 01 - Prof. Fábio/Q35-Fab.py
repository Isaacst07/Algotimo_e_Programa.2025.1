# Entrada 

n = int (input ('Número: '))

# Processamento

m = n // 1000
c = (n % 1000) // 100
d = ((n % 1000) % 100) //10 
u = ((n % 10) % 10) % 10

soma = m + c + d + u

# Saída

print (f'A soma dos elementos do número {n} é igual a {soma}. ')