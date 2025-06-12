import math

def main():
    pi_estimado = estimate_pi()
    pi_real = math.pi
    erro = abs(pi_real - pi_estimado)

    print(f"Estimativa de pi: {pi_estimado}")
    print(f"Valor real de pi: {pi_real}")
    print(f"Erro absoluto   : {erro:.15e}")


def estimate_pi():
    k = 0
    total = 0
    factor = (2 * math.sqrt(2)) / 9801

    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = (math.factorial(k) ** 4) * (396 ** (4 * k))
        term = factor * num / den
        total += term

        if term < 1e-15:
            break
        k += 1

    return 1 / total


main()