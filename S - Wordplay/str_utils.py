#n8n
def verificar_tamanho(tamanho: int, arquivo):
    contador = 0
    contador_filtro = 0
    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if len(palavra) >= tamanho:
            print(palavra)
            contador_filtro += 1

    percentual = (contador_filtro / contador) * 1000
    print(f'Percentual de palavras de tamanho {tamanho}: {contador_filtro}/{contador} - ({percentual:.2f}%)')


def has_no_caractere(caractere :str, arquivo):
    contador = 0 
    contador_filtro = 0
    for linha in arquivo:
        contador += 1
        palavra = linha.strip()
        if caractere.strip() not in palavra:
            contador_filtro += 1
            print(linha)

    percentual = (contador_filtro / contador) * 100
    print(f'Percentual de palavras sem o a letra "{caractere}": {contador_filtro}/{contador} - ({percentual:.2f}%)')


def uses_only(palavra, letras_permitidas):
    for letra in palavra:
        if letra in letras_permitidas:
            return True 

    return False


def nao_contem_letra(palavra, letras_permitidas):
 ...