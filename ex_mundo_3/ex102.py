#Criando uma função que calcula o fatórial e tem uma opção extra de mostrar ou não o cálculo

def fatorial(x, show=False):
    f = 1
    for i in range(x, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        f *= i
    return f

print(fatorial(15, show=True))