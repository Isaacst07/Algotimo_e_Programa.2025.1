from collections import deque

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        blocos = list(map(int, input().split()))
        
        visitado = [False] * (M + 1)
        fila = deque()
        fila.append((0, 0))  
        visitado[0] = True

        while fila:
            atual, passos = fila.popleft()

            if atual == M:
                print(passos)
                break

            for bloco in blocos:
                proximo = atual + bloco
                if proximo <= M and not visitado[proximo]:
                    visitado[proximo] = True
                    fila.append((proximo, passos + 1))


main()
