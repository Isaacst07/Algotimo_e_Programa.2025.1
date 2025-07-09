def main():
    i = 0.0

    while i < 1.8 :
        for j in range(1, 4):
        
            if i == int(i):
                print(f"I={int(i)} J={int(i) + j}")
            else:
                print(f"I={i:.1f} J={i + j:.1f}")
        i += 0.2

    print('I=2 J=3')
    print('I=2 J=4')
    print('I=2 J=5')


main()