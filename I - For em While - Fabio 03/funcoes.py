import os

def obter_numero_real(label: str):
  return float(input(label))


def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

def obter_numero_interio_min(label:str, min:int):
 numero = obter_numero_inteiro(label) 
 if  numero >= min:
    return numero
 else:
    print(f'O número é invalidado deve ser no mínimo {min} !')
    return obter_numero_interio_min(label, min)
 

def voto_certo():
  voto = obter_numero_inteiro('Qual o seu voto(1, 2, 3, 9, 0)? ')
  while voto != 1 or voto != 2 or voto != 3 or voto != 9 or voto != 0:
    print(f'''O voto informado não é válido, somente 1, 2, 3, 9, 0. Sendo:
1 - Candidato 1;
2 - Candidato 2;
3 - Candidato 3;
9 - Voto nulo;
0 - Voto em branco.
''')
    voto_certo()
 

def limpar_tela():
  os.system('cls')
  