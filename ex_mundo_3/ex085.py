#Lê 7 valores coloca em uma lista, depois separa em dus outras listas com os pares e impares e retorna eles em ordem

numeros = [[], []]
temp = 0

for i in range(1, 8):
    
    temp = int(input(f"Me fale o {i}º número: "))

    if temp % 2 == 0:
        numeros[0].append(temp)
    else:
        numeros[1].append(temp)
        
numeros[0].sort()
numeros[1].sort()

print(f"Os números pares são {numeros[0]}")
print(f"Os números ímpares são {numeros[1]}") 