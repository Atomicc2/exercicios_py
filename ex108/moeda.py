def dobro(num=0):
    resultado = num * 2
    return resultado

def metade(num=0):
    resultado = num / 2
    return resultado

def aumentar_10(num=0):
    resultado = num * 1.10
    return resultado

def diminuir_10(num=0):
    resultado = num * 0.9
    return resultado

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')