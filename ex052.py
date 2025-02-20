#Lendo se o número é primo ou não

number = int(input("Digite um número: "))
total = 0
for i in range(1, number + 1):
    if number % i == 0:
        total += 1
if total == 2 or total == 1:
    print("Esse número é primo")
else:
    print("Esse número não é primo")