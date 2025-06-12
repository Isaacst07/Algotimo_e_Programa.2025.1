import utils


def main():
    utils.limpar_tela()

    numero = utils.obter_numero_inteiro_min('Digite um número: ', 999)

    utils.limpar_tela()

    print(casas_decimais(numero))


def casas_decimais(numero: int):

    if numero <= 9:
        if numero == 1:
            return f'{numero} = {numero} unidade'
        else:
            return f'{numero} = {numero} unidades'
        
    elif numero <= 99:
        dezenas = numero // 10
        unidades = (numero % 10) / 1
        if dezenas != 1 and unidades != 1:
            return f'{numero} = {dezenas} dezenas e {unidades:.0f} unidades'
        elif dezenas == 1 and unidades != 1:
            return f'{dezenas} dezena e {unidades:.0f} unidades'
        elif dezenas != 1 and unidades == 1:
            return f'{dezenas} dezenas e {unidades:.0f} unidade'
        else:
            return f'{dezenas} dezena e {unidades:.0f} unidade'
        
    else: numero <= 999
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 10) / 1

    if centenas == 1 and dezenas == 1 and unidades == 1:
        return f'{numero} = {centenas} centena, {dezenas:.0f} dezena e {unidades:.0f} unidade'
    elif centenas == 1 and dezenas == 1 and unidades != 1:
        return f'{numero} = {centenas} centena, {dezenas:.0f} dezena e {unidades:.0f} unidades'
    elif centenas == 1 and dezenas != 1 and unidades != 1:
        return f'{numero} = {centenas} centena, {dezenas:.0f} dezenas e {unidades:.0f} unidades'
    elif centenas == 1 and dezenas != 1 and unidades == 1:
        return f'{numero} = {centenas} centena, {dezenas:.0f} dezenas e {unidades:.0f} unidade'
    elif centenas != 1 and dezenas == 1 and unidades == 1:
        return f'{numero} = {centenas} centenas, {dezenas:.0f} dezena e {unidades:.0f} unidade'
    elif centenas != 1 and dezenas != 1 and unidades == 1:
        return f'{numero} = {centenas} centenas, {dezenas:.0f} dezenas e {unidades:.0f} unidade'
    else:
        return f'{numero} = {centenas} centenas, {dezenas:.0f} dezenas e {unidades:.0f} unidades'

    
main()