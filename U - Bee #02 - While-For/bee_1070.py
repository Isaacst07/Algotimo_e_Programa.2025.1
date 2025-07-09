def main():
    x = int(input())

    for i in range (1, 7, 1):
        if x % 2 == 0:
            x += 1
            print(x)
            x += 2
        else:
            print(x)
            x += 2

              
main()