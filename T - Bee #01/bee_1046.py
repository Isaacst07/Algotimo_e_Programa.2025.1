def main(): 
    inicio, fim = map(int, input().split())

    duracao = duracao_da_partida(inicio, fim)
    print(f"O JOGO DUROU {duracao} HORA(S)")


def duracao_da_partida(inicio: int, fim: int):
    if inicio < fim:
        return fim - inicio
    elif inicio > fim:
        return (24 - inicio) + fim
    else:
        return 24
    

main()