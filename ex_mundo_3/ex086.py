#lê as entradas e cria uma matriz

temp = []
final =[]

for x in range(0, 3):

    for y in range(0, 3):
        temp.append(int(input(f"Digite o valor para [{y}, {x}]: ")))
    final.append(temp[:])    
    temp.clear()

for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{final[x][y]:^4}]", end='')
    print()