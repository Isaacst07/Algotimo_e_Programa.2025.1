from funcoes import obter_numero_real

def main():
    x = obter_numero_real('Dígite a coordenada cartesiana x: ')
    y = obter_numero_real('Dígite a coordenada cartesiana y: ')

    if area_retangulo(x, y) > 0:
        return print(f'A área do retângulo é {area_retangulo(x, y)}')
    else: area_retangulo(x, y) < 0
    return print(f'A área do retângulo é {area_retangulo(x, y) * (-1)}')


def area_retangulo(base, altura):
   return base * altura


main()