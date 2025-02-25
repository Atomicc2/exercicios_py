#Refazendo o mesmo do exercicio passado, porém agora retornando alguns valores

temp = []
final = []
valores_pares = 0
soma_terceira_coluna = 0
maior_valor = 0

for x in range(0, 3):

    for y in range(0, 3):
        n = int(input(f"Digite o valor [{x}, {y}]: "))
        temp.append(n)

        if n % 2 == 0:
            valores_pares += n
            
        if y == 2:
            soma_terceira_coluna += n

    if x == 1:
        if n > maior_valor:
            maior_valor = n

    final.append(temp[:])
    temp.clear()

for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{final[x][y]:^4}]", end='')
    print()
    
print(f"Os valores pares somados deram {valores_pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda coluna é {maior_valor}")