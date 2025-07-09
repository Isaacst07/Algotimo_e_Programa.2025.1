def main():
    n = int(input())
    qtd_rato = 0
    qtd_sapo = 0
    qtd_coelho = 0
    total_cobaia = 0

    for i in range (0, n, 1):
        parte1, cobaia = map(str, input().split())
        qtd = int(parte1)
        
        if cobaia == 'R':
            qtd_rato += qtd
        elif cobaia == 'S':
            qtd_sapo += qtd
        else:
            qtd_coelho += qtd
        
        total_cobaia += qtd

    percentual_coelho = (qtd_coelho / total_cobaia) * 100
    percentual_sapo = (qtd_sapo / total_cobaia) * 100
    percentual_rato = (qtd_rato / total_cobaia) * 100

    print(f'Total: {total_cobaia} cobaias')
    print(f'Total de coelhos: {qtd_coelho}')
    print(f'Total de ratos: {qtd_rato}')
    print(f'Total de sapos: {qtd_sapo}')
    print(f'Percentual de coelhos: {percentual_coelho:.2f} %')
    print(f'Percentual de ratos: {percentual_rato:.2f} %')
    print(f'Percentual de sapos: {percentual_sapo:.2f} %')


main()