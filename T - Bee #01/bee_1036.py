def main():
    a, b, c = map(float, (input()).split())

    resultado = calcular_bhaskara(a, b, c)
    print(resultado)
    

def calcular_bhaskara(a: float, b: float, c: float):
    delta = (b ** 2) - 4 * a * c

    if delta < 0 or a == 0:
        return 'Impossivel calcular'
    else:
        r1 = (-b + (delta ** (1/2))) / (2 * a)
        r2 = (-b - (delta ** (1/2))) / (2 * a)
        return f'R1 = {r1:.5f}\nR2 = {r2:.5f}'
    

main()