number = int(input("Say a number: "))

number_pair = number % 2                      #Utilizei o resto da divisão para confirmar 

if number_pair == 0:
    print(f"This number {number} is par")
else:
    print(f"This number {number} is impar")