def main():
    salario = float(input())

    calcular_reajuste(salario)


def calcular_reajuste(salario: float):

    if salario <= 400:
        percentual = 15
        reajuste = salario * (percentual / 100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
    elif salario <= 800:
        percentual = 12
        reajuste = salario * (percentual / 100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
    elif salario <= 1200:
        percentual = 10
        reajuste = salario * (percentual / 100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
    elif salario <= 2000:
        percentual = 7
        reajuste = salario * (percentual / 100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
    else:
        percentual = 4
        reajuste = salario * (percentual / 100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')


main()