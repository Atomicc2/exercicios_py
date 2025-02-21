#Lê vários número e retorna a soma deles, condição de parada: digitar 999

print("O botão de desligar é [ - 999 -]")

soma = 0
total = -1
num = 0

while num != 999:
    soma += num
    total += 1
    num = int(input("Digite os número que deseja somar: "))
    
print(f"Você digitou {total} numeros e a suma foi {soma}")
