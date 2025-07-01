def main():
    code, qtd = map(int, (input()).split())

    valor_compra = calcular_conta(code, qtd)
    print(valor_compra)


def calcular_conta(code: int, qtd: int):
    if code == 1:
        conta = 4 * qtd
        return f'Total: R$ {conta:.2f}'
    elif code == 2:
        conta = 4.50 * qtd
        return f'Total: R$ {conta:.2f}'
    elif code == 3:
        conta = 5 * qtd
        return f'Total: R$ {conta:.2f}'
    elif code == 4:
        conta = 2 * qtd
        return f'Total: R$ {conta:.2f}'
    elif code == 5:
        conta = 1.50 * qtd
        return f'Total: R$ {conta:.2f}'
    

main()