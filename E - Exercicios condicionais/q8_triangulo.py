from funcoes import obter_numero_inteiro

def main():
  lado_a = obter_numero_inteiro('Primeiro lado do triângulo: ')
  lado_b = obter_numero_inteiro('Segundo lado do triângulo:  ')
  lado_c = obter_numero_inteiro('Terceiro lado do triângulo: ')
  print('                                                         ')
  angulo_1 = obter_numero_inteiro('Primeiro ângulo do triângulo: ')
  angulo_2 = obter_numero_inteiro('Segundo ângulo do triângulo: ')
  angulo_3 = obter_numero_inteiro('Terceiro ângulo do triângulo: ')



  eh_triangulo(lado_a, lado_b, lado_c, angulo_1, angulo_2, angulo_3)



def eh_triangulo(lado_a, lado_b, lado_c, angulo_1, angulo_2, angulo_3): 
  if lado_a + lado_b >= lado_c and lado_a + lado_c >= lado_b and lado_b + lado_c >= lado_a:
   return print(f'Sendo esse triângulo também {classificar_triangulo_lado(lado_a, lado_b, lado_c)} e s9eu perímetro é {lado_a + lado_b + lado_c}. {classificar_triangulo_angulo(angulo_1, angulo_2, angulo_3, lado_a, lado_b, lado_c)}')
  else:
    return print('Seus lados não formar triângulo!')




def calcular_perimetro(lado_a, lado_b, lado_c):
  return lado_a + lado_b + lado_c


def calcular_area(lado_a, lado_b, lado_c):
  p = (lado_a + lado_b + lado_c) / 2 
  return (p * (p - lado_a) * (p - lado_b) * (p - lado_c) ) ** (1/2)


def forma_triangulo(angulo_1, angulo_2, angulo_3):
  if angulo_1 + angulo_2 + angulo_3 == 180:
    return True 
  else:
    return False 


def classificar_triangulo_angulo(angulo_1, angulo_2, angulo_3, lado_a, lado_b, lado_c):
  if angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90 and forma_triangulo(angulo_1, angulo_2, angulo_3) == True:
    return print(f'Forma um triângulo que é RETÂNGULO de área {calcular_area(lado_a, lado_b, lado_c):.2f}')
  elif angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90 and forma_triangulo(angulo_1, angulo_2, angulo_3) == True:
    return print(f'Forma um triângulo ACUTÂNGULO de área {calcular_area(lado_a, lado_b, lado_c):.2f}')
  elif angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90 and forma_triangulo(angulo_1, angulo_2, angulo_3) == True: 
    return print(f'Forma um triângulo OBTUSÂNGULO de área {calcular_area(lado_a, lado_b, lado_c):.2f}')
  

def classificar_triangulo_lado(lado_a, lado_b, lado_c):
  if lado_a == lado_b and lado_b == lado_c:
    return 'EQUILÁTERO'
  elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    return 'ESCALENO'
  else:
    return 'ISÓSCELES'


main()