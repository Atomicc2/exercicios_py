#Soma de inteiros
soma = 0
for i in range(1, 7):
    numbers = int(input("Give-me a six number: "))
    if numbers % 2 == 0:
        soma += numbers
print(f"The sum of even nnumbers is: {soma}")