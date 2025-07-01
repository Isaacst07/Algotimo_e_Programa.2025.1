def main():
    a, b, c = map(float, (input()).split())

    forma_triangulo(a, b, c)


def forma_triangulo(a: float, b: float, c: float):
    if a + b > c and a + c > b and b + c > a:
        perimetro = a + b + c
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area = ((a + b) * c) / 2
        print(f'Area = {area:.1f}')


main()