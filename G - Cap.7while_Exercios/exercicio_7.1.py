import math
import utils

def main():
   
    a_inicial = utils.obter_numero_real('Digite o valor inicial de "a": ')
    a_final = utils.obter_numero_real('Digite o valor final de "a": ')
    

    resultados = test_square_root(a_inicial, a_final)

    print(f'\n{'a':<4} {'mysqrt(a)':<14} {'math.sqrt(a)':<14} {'diff':<}')
   
    i = 0
    while i < len(resultados):
        a, my, real, diff = resultados[i]
        print(f"{a:<4.1f} {my:<14.12f} {real:<14.12f} {diff:.12e}")
        i += 1


def mysqrt(a):
    x = a / 2.0  
    epsilon = 1e-15
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def test_square_root(a_inicial: float, a_final: float):
    results = []
    a = a_inicial
    while a <= a_final:
        my = mysqrt(a)
        real = math.sqrt(a)
        diff = abs(my - real)
        results.append((a, my, real, diff))
        a += 1.0
    return results


main()