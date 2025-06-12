def main():
    altura = obter_numero_real('Sua altura: ')
    peso = obter_numero_real('Seu peso: ')

    imc = calcular_imc(peso, altura)

    classificacao = classificacao_imc(imc)

    print (f'Com sua altura {altura:.2f}m e seu peso {peso}kg seu imc é {imc:.2f} .')
    print (f'Então, você está {classificacao}.')


def calcular_imc(peso, altura):
    return peso / altura ** 2 


def classificacao_imc(imc: float):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'Sobre peso'
    elif imc <= 34.9:
        return 'Obesidade grau 1'
    elif imc <= 39.9:
        return 'Obesidade grau 2'
    else: imc > 40.0
    return 'Obesidade grau 3'


def obter_numero_real(label: str):
  return float(input(label))


main()