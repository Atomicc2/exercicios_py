#Comparando números inteiros

number = int(input("Me fale um número: "))
number2 = int(input("Me fale outro número: "))

if number > number2:
    print(f"O número {number} é maior que o número {number2}")
elif number2 > number:
    print(f"O número {number2} é maior que o número {number}")
else:
    print("Os números são iguais!!")