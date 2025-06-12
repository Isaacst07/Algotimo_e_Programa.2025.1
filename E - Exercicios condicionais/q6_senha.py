def main():

    print('Pré_requisitos para a senha:') 
    print('Conter no minímo 8 caracteres;')
    print('Conter letras tanto maiusculas(A) quanto minúsculas(a);')
    print('Conter um número ou mais;')
    print('E conter um simbolo(!@#$%&*).')

    print('                                                              ')
    print('                                                              ')
    
    senha = obter_senha('Informe sua senha:')
    senha_eh_valida = eh_valida(senha)
    print(f'{senha_eh_valida}.')


def verificador_tamanho(senha):
    numero_caracteres = 0 
    numero = 0
    for numero_caracteres in senha:
        numero = numero + 1 
    if numero < 8:
        return False
    else:
        return True


def letra_eh_maiscula(senha):
    for c in senha: 
        if c >= 'A' and c <= 'Z':
           return True 
    return False 


def letra_eh_minuscula(senha):
    for i in senha: 
        if i >= 'a' and i <= 'z':
           return True 
    return False 


def tem_numero(senha):
    for i in senha: 
        if i >= '0' and i <= '9':
           return True 
    return False 


def tem_carcteres_especial(senha):
    carcteres_especial = '!@#$%&*'
    for i in senha:
        if i in carcteres_especial:
            return True
        return False
    

def eh_valida(senha):
    if verificador_tamanho(senha) and letra_eh_maiscula(senha) and letra_eh_minuscula(senha) and tem_numero(senha) and tem_carcteres_especial(senha):
        return 'A sua senha é VÁLIDA'
    else:
        return 'Sua senha NÃO É VÁLIDA'
    

def obter_senha(label:str):
    return input(label)
    

main()


























def obter_senha(label:str):
    return input(label)


main()