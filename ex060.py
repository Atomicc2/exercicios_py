#Fazendo o cálculo de fatorial

numero = total = int(input("Me fale um número: "))

while numero != 1:
    numero -= 1
    total *= numero

print(f"O fatorial desse número é: {total}")

