def main():
    m = int(input())
    a = int(input())
    b = int(input())

    mais_velho(m,a,b)

    
def mais_velho(m: int, a: int, b:int):
    x = m - a - b

    if x > a and x > b:
        print(x)
    elif a > b and a > x:
        print(a)
    else:
        print(b)


main()