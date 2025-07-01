def main():
    salario = float(input())

    calcular_imposto_de_renda(salario)


def calcular_imposto_de_renda(salario: float):
    imposto = 0

    if salario <= 2000:
        print('Isento')
        
    else:
        if salario <= 3000:
            imposto += (salario - 2000) * 0.08
            print(f'R$ {imposto:.2f}')

        elif salario <= 4500:
            imposto += (1000 * 0.08) 
            imposto += (salario - 3000) * 0.18
            print(f'R$ {imposto:.2f}')

        else:
            imposto += (1000 * 0.08)  
            imposto += (1500 * 0.18)  
            imposto += (salario - 4500) * 0.28

            print(f'R$ {imposto:.2f}')


main()