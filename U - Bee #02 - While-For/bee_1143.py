def main():
    n = int(input())
    number = 1

    for i in range (0, n, 1):
        print(f'{number} {number**2} {number * (number**2)}')

        number +=1


main()