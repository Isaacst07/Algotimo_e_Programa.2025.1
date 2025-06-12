def main():
  lado_1 = obter_numero_inteiro('Qual tamanho do primeiro lado do triângulo:')
  lado_2 = obter_numero_inteiro('Qual tamanho do segundo lado do triângulo:')
  lado_3 = obter_numero_inteiro('Qual tamanho do terceiro lado do triângulo:')

  hipotenusa_e_catetos(lado_1, lado_2, lado_3)
  
  
def hipotenusa_e_catetos(lado_1, lado_2, lado_3):
  if lado_1 > lado_2 and lado_1 > lado_3:
    return print(f'A hipotenusa é o lado 1, que é igual a {lado_1} e os lados 2 e 3 são os catetos,respectivamente iguais a {lado_2} e {lado_3}')
  elif lado_2 > lado_1 and lado_2 > lado_3:
    return print(f'A hipotenusa é o lado 2, que é igual a {lado_2} e os lados 1 e 3 são os catetos,respectivamente iguais a {lado_1} e {lado_3}')
  else: lado_3 > lado_1 and lado_3 > lado_2
  return print(f'A hipotenusa é o lado 3, que é igual a {lado_3} e os lados 1 e 2 são os catetos,respectivamente iguais a {lado_1} e {lado_2}')
 

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()