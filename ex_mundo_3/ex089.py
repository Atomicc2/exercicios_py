#Lê as notas dos alunso, tira a média e da a possibilidade de ver as notas de alguém depois

temp = []
final = []

while True:

    temp.append(str(input("Nome: ")))
    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))

    final.append(temp[:])
    temp.clear()

    respostas = str(input("Quer continuar? [S/N] "))
    if respostas in 'Nn':
        break

print("-=-" * 10)
print(f"{'Nº':<4}{'Nome':<15}{'Média':<5}")
print("---" * 10)

for i in range(0, len(final)):
    media = (final[i][1] + final[i][2]) / 2 
    print(f"{i:<4}{final[i][0]:<15}{media:<5}")
    
print("---" * 10)
print("-=-" * 10)

while True:

    n = int(input("Mostrar nota de qual aluno? (999 interrompe o software) "))
    if n == 999:
        break
    print(f"As notas do aluno {final[n][0]} foram [{final[n][1]}] e [{final[n][2]}]")