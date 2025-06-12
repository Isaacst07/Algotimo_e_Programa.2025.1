import os
import time




def obter_numero_real(label: str):
  return float(input(label))


def obter_str(label: str):
  return str(input(label))


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
 

def numero_certo(label: str):
  numero = obter_numero_inteiro(label)
  if numero == 1 or numero == 2 :
    return numero
  else:
    print(f'Opção inválida, dígite - 1 para sim ou 2 para não')
    numero_certo('Gostou? 1-sim/2-não: ')


def obter_numero_entre(label: str, min: int, max: int):
  numero = obter_numero_real(label)

  if numero >= min and numero <= max:
    return numero
  else: 
    print(f'A nota {numero:.1f} não é válida, as notas são entre {min:.1f} e {max:.1f} !')
    

def limpar_tela():
  os.system('cls')


def delay(duracao: int):
  time.sleep(duracao / 1000)



  