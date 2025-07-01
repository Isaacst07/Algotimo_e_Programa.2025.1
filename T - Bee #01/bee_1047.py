def main():
    hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

    calcular_duracao(hora_inicio, minuto_inicio, hora_fim, minuto_fim)


def calcular_duracao(hora_inicio: int, minuto_inicio: int, hora_fim: int, minuto_fim: int):
    inicio_total = hora_inicio * 60 + minuto_inicio
    fim_total = hora_fim * 60 + minuto_fim

    if fim_total > inicio_total:
        duracao_partida = fim_total - inicio_total
    else:
        duracao_partida = (24 * 60 - inicio_total) + fim_total
    
    duracao_horas = duracao_partida// 60
    duracao_minutos = duracao_partida % 60

    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")


main()