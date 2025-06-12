def main():
 coeficiente_a = obter_numero_inteiro('Digite o valor coeficiente "a" da equação do 2°: ')
 coeficiente_b = obter_numero_inteiro('Digite o valor coeficiente "b" da equação do 2°: ')
 coeficiente_c = obter_numero_inteiro('Digite o valor do coeficiente "c" da equação do 2°:')

 calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)


def calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c):
 delta = coeficiente_b * coeficiente_b - 4 * coeficiente_a * coeficiente_c
 if delta < 0 :
   return print(f'A equação não terá raízes reais, pois delta é igual a zero! ')
 elif delta == 0 :
   x = -coeficiente_b / (2 * coeficiente_a)
   return print(f'A equação só possui uma raiz real: x1 = {x}')
 else:
   x1 = (-coeficiente_b + (delta ** (1 / 2))) / (2 * coeficiente_a)
   x2 = (-coeficiente_b - (delta ** (1 / 2))) / (2 * coeficiente_a)
   return print(f'A equação possui duas raízes x1 = {x1:.2f} e x2 = {x2:.2f} !')

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

main()