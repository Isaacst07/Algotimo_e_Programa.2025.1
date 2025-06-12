# Entrada 

peso = int (input ('Qual o seu peso: '))
altura = float (input ('Qual a sua altura: '))

# Processamento

imc = peso / (altura * altura)

# Saída

print (f'O seu IMC será de {imc:.2f} .')