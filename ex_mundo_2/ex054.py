#Verificador de maior idade
maiores = 0
for i in range(1, 8):
    idade = int(input("Me informe aas idades: "))
    if idade >= 21:
        maiores += 1
print(f"{maiores} de vocês é maior de idade!")