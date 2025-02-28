def dobro(num=0, format=False):
    resultado = num * 2
    return resultado if not format else moeda(resultado)

def metade(num=0, format=False):
    resultado = num / 2
    return resultado if not format else moeda(resultado)

def aumentar_10(num=0, format=False):
    resultado = num * 1.10
    return resultado if not format else moeda(resultado)

def diminuir_10(num=0, format=False):
    resultado = num * 0.9
    return resultado if not format else moeda(resultado)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')