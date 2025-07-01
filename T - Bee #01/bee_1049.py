def main():
    palavra1 = input()
    palavra2 = input()
    palavra3 = input()

    qual_o_animal(palavra1, palavra2, palavra3)


def qual_o_animal(palavra1: str, palavra2: str, palavra3: str):

    if palavra1 == 'vertebrado':
        if palavra2 == 'ave':
            if palavra3 == 'carnivoro':
                print('aguia')
            else:
                print('pombo')
        else:
            if palavra3 == 'onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        if palavra2 == 'inseto':
            if palavra3 == 'hematofago':
                print('pulga')
            else:
                print('lagarta')
        else:
            if palavra3 == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')


main()