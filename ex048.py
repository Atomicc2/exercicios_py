#soma de todos os números multiplos de 3 entre 1 e 500
valor = 0
for i in range(1, 501, 2):
    if (i % 3) == 0:
        valor += i
print(valor)