import funcoes

def main():
    eleitores = funcoes.obter_numero_inteiro('Quantidade de eleitores: ')
    contador = 1
    canditado_1 = 0 
    canditado_2 = 0 
    canditado_3 = 0
    voto_nulo = 0
    voto_branco = 0 

    while contador <= eleitores:
       voto = voto_certo()
       contador += 1

       if voto == 1:
            canditado_1 += 1
       elif voto == 2:
            canditado_2 += 1
       elif voto == 3:
            canditado_3 += 1
       elif voto == 9:
            voto_nulo += 1 
       else:
            voto_branco += 1

        

    print(f'''-------------RESULTADO ELEIÇÃO-------------
a) Total de votos para os candidatos:
Candidato 1: {canditado_1} votos
Candidato 2: {canditado_2} votos
Candidato 3: {canditado_3} votos

b) Total de votos nulos: {voto_nulo} votos

c) Total de votos em branco: {voto_branco} votos

d) Quem venceu a eleicao: {quem_venceu(canditado_1, canditado_2, canditado_3)}
PARABÉNS!!!!

''')
    

def quem_venceu(candidato_1, candidato_2, candidato_3):
    if candidato_1 > candidato_2 and candidato_1 > candidato_3:
       return 'O vencedor foi o candidato 1'
    if candidato_2 > candidato_1 and candidato_2 > candidato_3:
       return 'O vencedor foi o candidato 2'
    if candidato_3 > candidato_1 and candidato_3 > candidato_2:
       return 'O vencedor foi o candidato 3'


def voto_certo():
  voto = funcoes.obter_numero_inteiro('Qual o seu voto(1, 2, 3, 9, 0)? ')
  
  if voto == 1 or voto == 2 or voto == 3 or voto == 9 or voto == 0:
        return voto
  else:
    print(f'''O voto informado não é válido, somente 1, 2, 3, 9, 0. Sendo:
1 - Candidato 1;
2 - Candidato 2;
3 - Candidato 3;
9 - Voto nulo;
0 - Voto em branco.
''')
    voto_certo()
      

main()