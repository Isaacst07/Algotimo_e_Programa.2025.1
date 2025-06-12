def main():
    altura = obter_numero_real('Sua altura(m): ')
    peso = obter_numero_real('Seu peso(kg): ')

    imc = calcular_imc(peso, altura)

    classificacao = classificacao_imc(imc)

    print (f'Com sua altura {altura:.2f}m e seu peso {peso}kg seu imc é {imc:.2f} .')
    print (f'Então, você está {classificacao}.')


def calcular_imc(peso, altura):
    return peso / altura ** 2 


def classificacao_imc(imc: float):
    if imc < 25:
        return 'com o peso normal'
    elif imc <= 30:
        return 'obeso'
    else: imc > 30
    return 'Obesidade mórbida'


def obter_numero_real(label: str):
  return float(input(label))


main()