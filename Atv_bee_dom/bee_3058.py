def main():
    n = int(input())

    menor_preco_por_kg = float('inf')

    for i in range (n):
        line_input = input()
        parts = line_input.split()
        p = float(parts[0])
        g = float(parts[1])
        preco_atual_por_kg = (p / g) * 1000

        if preco_atual_por_kg < menor_preco_por_kg:
            menor_preco_por_kg = preco_atual_por_kg

    print(f'{menor_preco_por_kg:.2f}')


main()