def main():
    dia_inicio = int(input().split()[1])
    hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(' : '))

    dia_fim = int(input().split()[1])
    hora_fim, minuto_fim, segundo_fim = map(int, input().split(' : '))
    
    calcular_duracao(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim)


def calcular_duracao(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim):

    inicio_total_segundos = dia_inicio * 24 * 3600 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
    fim_total_segundos = dia_fim * 24 * 3600 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim

    duracao_total = fim_total_segundos - inicio_total_segundos
    
    dias = duracao_total // (24 * 3600)
    duracao_total %= (24 * 3600)

    horas = duracao_total // 3600
    duracao_total %= 3600

    minutos = duracao_total // 60
    segundos = duracao_total % 60

    print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')


main()