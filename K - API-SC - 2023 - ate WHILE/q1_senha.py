import funcoes
from random import randint


def main():
  
  print('Vamos gerar uma senha?')
  
  
  num_digitos = funcoes.obter_numero_inteiro('Quantidade de dígitos da senha: ')

  senha = gerar_senha(num_digitos)
  funcoes.limpar_tela()
  print(f'Sua senha é essa: {senha}')
  
  
  gostou = funcoes.numero_certo('Você gostou? 1 - Sim, 2 - Não: ')

  while gostou != 1:
    print('Tudo bem! vou gerar um nova pra você.')
    
    senha = gerar_senha(num_digitos)
    print(f'Sua nova senha é essa: {senha}')
    
    gostou = funcoes.numero_certo('Você gostou? 1 - Sim, 2 - Não: ')
    funcoes.limpar_tela()

  funcoes.limpar_tela()
  print('Que bom que você gostou!')
  print('Se precisar de uma nova senha volte aqui!')
 
  print('Fim.')


def gerar_senha(tamanho: int):
  senha = ''
  carac_anterior = ''
  while len(senha) < tamanho:
    carac_atual = str(randint(0, 9))

    if carac_anterior == '' or (carac_atual != carac_anterior and caracteres_diferentes(carac_atual, carac_anterior) > 1):
      
      carac_anterior = carac_atual
      senha = senha + carac_atual
    else:
      
     print()
  
  return senha


def caracteres_diferentes(valor1: str, valor2: str) -> int:
  a = int(valor1)
  b = int(valor2)

  diff = a - b

  if a >= b:
    return diff
  else:
    return -1 * diff


main()