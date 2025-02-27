#criando uma função que faz o cálculo da área

def calculo_area(l, c):
    area = l * c
    print(f"A área do terreno é {area:.2f} Metros Quadrados")
    
def linhas(a):
    print(f"-" * a)

linhas(20)
largura = float(input("Largura do terreno: "))
comprimento = float(input("Comprimento do terreno: "))
linhas(20)
calculo_area(largura, comprimento)
linhas(20)