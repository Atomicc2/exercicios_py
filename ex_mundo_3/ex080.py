#Lê 5 entradas de números e retorna eles ordenados sem usar o .sort()
lista = []
for i in range(0, 5):
    n = int(input("Digite a entrada: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                break
            posição += 1 
        
print(lista)