# Entrada 

custo_do_carro = float (input('Valor do carro: '))
percetagem_do_distribuidor = int (input ('Percetagem do distribuidor: '))
impostos = int (input ('Valor dos impostos: '))

# Processamento

valor_distribuidor = (custo_do_carro / 100) * percetagem_do_distribuidor
valor_impostos = ((custo_do_carro + valor_distribuidor) / 100) * impostos
custo_final = custo_do_carro + valor_distribuidor + valor_impostos

# Saída

print (f'O custo final do carro após os impostos será de {custo_final:.2f}R$. ')