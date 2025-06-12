from funcoes import obter_numero_inteiro

def main():
    temperatura = obter_numero_inteiro('Insira a temperatura: ')
    tipo_temperatura  = str(input('Essa temperatura é [C°/F°/K°]: '))
    converte_para = str(input('E para qual temperatura você vai converter[C°/F°/K°]: '))

    converte_temperaturas(temperatura, tipo_temperatura, converte_para)


def de_celsisus_para_demais(temperatura, converte_para):
    if converte_para == 'F°' or converte_para == 'F' or converte_para == 'f°' or converte_para == 'f' and temperatura >= -273.15:
        return print(f'A temperatura {temperatura}°C de Celsius para Fahrenheit é {(temperatura * (9/5) + 32):.2f}°F ')
    elif converte_para == 'K°' or converte_para == 'K' or converte_para == 'k°' or converte_para == 'k' and temperatura >= -273.15:
        return print(f'A temperatura {temperatura}°C de Celsius para Kelvin é {(temperatura + 273.15):.2f}°K ')
    elif converte_para == 'C°' or converte_para == 'C' or converte_para == 'c°' or converte_para == 'c' and temperatura >= -273.15:
        return print(f'A temperatura {temperatura}°C de Celsius para Celsius é {temperatura:.2f}°C ')
    

def de_fahrenheit_para_demais(temperatura, converte_para):
    if converte_para == 'F°' or converte_para == 'F' or converte_para == 'f°' or converte_para == 'f' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°F de Fahrenheit para Fahrenheit é {temperatura:.2f}°F ')
    elif converte_para == 'K°' or converte_para == 'K' or converte_para == 'k°' or converte_para == 'k' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°F de Fahrenheit para Kelvin é {((temperatura + 459.67) * 5 / 9):.2f}°K ')
    elif converte_para == 'C°' or converte_para == 'C' or converte_para == 'c°' or converte_para == 'c' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°F de Fahrenheit para Celsius é {((temperatura - 32) * 5 / 9):.2f}°C ')


def de_kelvin_para_demais(temperatura, converte_para):
    if converte_para == 'F°' or converte_para == 'F' or converte_para == 'f°' or converte_para == 'f' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°k de Kelvin para Fahrenheit é {(((temperatura - 273.15) * 9 / 5) + 32):.2f}F° ')
    elif converte_para == 'K°' or converte_para == 'K' or converte_para == 'k°' or converte_para == 'k' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°K de Kelvin para Kelvin é {temperatura :.2f}°K ')
    elif converte_para == 'C°' or converte_para == 'C' or converte_para == 'c°' or converte_para == 'c' and temperatura >= 0:
        return print(f'A temperatura {temperatura}°K de Kelvin para Celsius é {(temperatura + 273.15):.2f}°C ')
    

def converte_temperaturas(temperatura, tipo_temperatura, converte_para):
    if tipo_temperatura == 'C°' or tipo_temperatura == 'C' or tipo_temperatura == 'c°' or tipo_temperatura == 'c':
        return de_celsisus_para_demais(temperatura, converte_para)
    elif tipo_temperatura == 'F°' or tipo_temperatura == 'F' or tipo_temperatura == 'f°' or tipo_temperatura == 'f':
        return de_fahrenheit_para_demais(temperatura, converte_para)
    else: tipo_temperatura == 'K°' or tipo_temperatura == 'K' or tipo_temperatura == 'k°' or tipo_temperatura == 'k'
    return de_fahrenheit_para_demais(temperatura, converte_para)


main()