def main():
    n = int(input())
    pum1 = 1
    pum2 = 2
    pum3 = 3

    for i in range(0 , n, 1):
        print(f'{pum1} {pum2} {pum3} PUM')

        pum1 += 4
        pum2 += 4
        pum3 += 4


main()