def main():
  numero = obter_numero_real('Informe um número que quer arredondar: ')
  resultado = arredondar(numero)
  print(f"O número {numero} arredondado é {resultado}")


def arredondar(numero):
    if numero - int(numero) >= 0.5:
        return int(numero) + 1
    else:
        return int(numero)


def obter_numero_real(label: str):
  return float(input(label))


main()