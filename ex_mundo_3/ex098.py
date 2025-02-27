#Fazendo um contador usando função
from time import sleep

def contador(start, stop, spacing):
    print(f"Contagem de {start} até {stop} de {spacing} em {spacing}")
    
    if spacing < 0:
        spacing *= -1
    if spacing == 0:
        spacing = 1

    cont = start
    if start <= stop:
        while cont <= stop:
            print(cont, end=' ', flush=True)
            cont += spacing
            sleep(0.2)
        print()
    else:
        while cont >= stop:
            print(cont, end=' ', flush=True)
            cont -= spacing
            sleep(0.2)
        print()
    
contador(1, 10, 1)
contador(10, 0, 2)

x = int(input("Start: "))
y = int(input("Stop: "))
z = int(input("Spacing: "))

contador(x, y, z)