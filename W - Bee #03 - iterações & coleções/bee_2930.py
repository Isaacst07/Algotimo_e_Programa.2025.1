def main():
    e, d = map(int, input().split())
    dias_faltando = d - e

    if dias_faltando >= 3:
        print('Muito bem! Apresenta antes do Natal!')
    elif dias_faltando < 3 and dias_faltando > 0:
        print('Parece o trabalho do meu filho!')
        if d + 2 <= 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')
    else:
        print('Eu odeio a professora!')


main()