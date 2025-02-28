def dobro(num=0, format=False):
    resultado = num * 2
    return resultado if not format else moeda(resultado)

def metade(num=0, format=False):
    resultado = num / 2
    return resultado if not format else moeda(resultado)

def aumentar_10(num=0, dim=0, format=False):
    resultado = num + ((dim / 100) * num)
    return resultado if not format else moeda(resultado)

def diminuir_10(num=0, aum=0, format=False):
    resultado = num - ((aum / 100) * num)
    return resultado if not format else moeda(resultado)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=0, aum=0, dim=0):
    print("---" * 15)
    print(f"  ANALIZANDO O PREÇO {moeda(num)}")
    print(f"O dobro é \t{dobro(num, format=True)}")
    print(f"A metade é \t{metade(num, format=True)}")
    print(f"{aum}% de aumento \t{aumentar_10(num, aum, format=True)}")
    print(f"{dim}% de redução \t{diminuir_10(num, dim, format=True)}")
    print("---" * 15)