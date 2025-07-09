def main():
    n = int(input()) 
    number1 = 1
    number2 = 1
    number3 = 1

    for i in range (0, n, 1):
        
        for x in range(0, 2, 1):
            if number1 == 1 and number2 == 2 and number3 == 1:
                print(f'{number1} {number2} {number3}')
            else:
                print(f'{number1} {number2} {number3}')

            number2 += 1
            number3 += 1
        
        number1 += 1
        number2 = (number1 ** 2)
        number3 = number1 * number2
        

main()