#Repetindo o ex009 porém usando um laço de repetição

numero = int(input("Me fale um número de 0 a 9: "))
print("-=-" * 4)
for i in range(0, 10):
    print(f"{numero} x {i} = {numero * i}")
print("-=-" * 4)