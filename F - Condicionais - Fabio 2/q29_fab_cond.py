from funcoes import obter_numero_inteiro

def main():
   numero = obter_numero_interio_min('Dígite um número inteiro: ')

   eh_quadrado_perfeito(numero)


def eh_quadrado_perfeito(numero):
   parte_um_numero = numero // 100
   parte_dois_numero = numero % 100
   if raiz_quadrada(numero) == (parte_um_numero + parte_dois_numero):
      return print(f'O número {numero} é quadrado perfeito!')
   else:
      return print(f'O número {numero} NÃO é quadrado perfeito!')



def raiz_quadrada(numero):
   return numero ** (1/2)


def obter_numero_interio_min(label:str ):
 numero = obter_numero_inteiro(label)
 min = 1000
 max = 9999
 if  min <= numero <= max:
    return numero
 else:
    print(f'O número deve ser no mínimo {min} e no máximo {max}')
    return print(obter_numero_interio_min(label))
  

   
main()