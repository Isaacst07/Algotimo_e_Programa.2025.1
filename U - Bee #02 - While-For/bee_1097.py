def main():
    i = 1
    j = 7

    while i <= 9:
        print(f'I={i} J={j}')
        j -= 1
        print(f'I={i} J={j}')
        j -= 1
        print(f'I={i} J={j}')

        j += 4
        i += 2


main()