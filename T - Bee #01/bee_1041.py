def main():
    x, y = map(float, (input()).split())

    qual_quadrante(x, y)
   

def qual_quadrante(x: float, y: float):
    if x == 0 and y == 0:
        print('Origem')
    elif x == 0:
        print('Eixo Y')
    elif y == 0:
        print('Eixo X')
    elif x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    else:
        print('Q4')
    

main()