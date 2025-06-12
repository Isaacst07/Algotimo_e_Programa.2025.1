def main():
 valor_da_compra = float(input('Valor da compra(R$): '))
 cliente_vip = str(input('Você é cliente vip?(sim/não): '))
 cLiente_aniversariante = str(input('Hoje é seu aniversário?(sim/não): '))

 valor_final = calcular_valor_final(valor_da_compra, cliente_vip, cLiente_aniversariante)
 
 print(f'Após os desconto o valor final da compra será de {valor_final:.2f}R$ . ')


def calcular_desconto_base(valor_da_compra):
  if valor_da_compra > 500:
    return (0.15)
  elif valor_da_compra >= 200:
    return (0.10)
  else:
    return (0.05)
  

def calcular_descontos_adiconais(cliente_vip, cliente_aniversariante):
  desconto = 0
  if cliente_vip == 'sim':
    desconto += (0.05)
  if cliente_aniversariante == 'sim':
    desconto += (0.03)  
    return desconto
  

def calcular_valor_final(valor_da_compra, cliente_vip, cliente_aniversariante):
  desconto_base = calcular_desconto_base(valor_da_compra)
  desconto_adicional = calcular_descontos_adiconais(cliente_vip, cliente_aniversariante)
  desconto_total = desconto_base + desconto_adicional
  return valor_da_compra - (valor_da_compra * desconto_total)
  

main ()