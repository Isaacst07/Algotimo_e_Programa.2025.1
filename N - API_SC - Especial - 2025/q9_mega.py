# comecei 22:00
# terminei 22:40
# Sábado

from q1_number_utils import limpar_tela


def main():
    premio = float(input('De quanto foi o prêmio da mega(R$): '))
    premio_apos_imposto = premio - (premio * 0.2)
    maior_colaboracao = 0
    menor_colaboracao = 0
    total_colaboracoes = 0

    limpar_tela()

    print('Digite "0" quando quiser parar!')



    while True:
        coloboracao = float(input('Colaboração desse amigo para o Prêmio(R$): '))
        total_colaboracoes += coloboracao

        if coloboracao == 0:
            break

        if maior_colaboracao == 0 or coloboracao > maior_colaboracao:
            maior_colaboracao += coloboracao
        
        if menor_colaboracao == 0 or coloboracao < menor_colaboracao:
            menor_colaboracao += coloboracao

    maior_premio = (maior_colaboracao / total_colaboracoes) * premio_apos_imposto
    menor_premio = (menor_colaboracao / total_colaboracoes) * premio_apos_imposto

    limpar_tela()

    print(f'''
1) O maior prêmio individual foi: R$ {maior_premio:.2f}
1) O menor prêmio individual foi: R$ {menor_premio:.2f}
''')

        
main()