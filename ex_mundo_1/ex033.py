print("Say three numbers: ")

number_1 = float(input("1º: "))
number_2 = float(input("2º: "))
number_3 = float(input("3º: "))

#Primeira forma usando comparativos nas própias condições

if number_1 > number_2 and number_1 > number_3:
    print("This is the biggest number: {}!".format(number_1))
elif number_2 > number_1 and number_1 > number_3:
    print("This is the bigest number: {}!".format(number_2))
else:
    print("this is the bigest number: {}!".format(number_3))

if number_1 < number_2 and number_1 < number_3:
    print("This is the smallest number: {}!".format(number_1))
elif number_2 < number_1 and number_1 < number_3:
    print("This is the smallest number: {}!".format(number_2))
else:
    print("This is the smallest number: {}!".format(number_3))

#Segunda forma usando uma variávela antes

max_num = number_1
min_num = number_1

if number_2 > max_num:
    max_num = number_2
if number_3 > max_num:
    max_num = number_3

if number_2 < min_num:
    min_num = number_2
if number_3 < min_num:
    min_num = number_3

print("This is the bigest number: {}!".format(max_num))
print("This is the smallest number: {}!".format(min_num))

#Terceira forma, a mais fácil, usando as função max e min

max_num1 = max(number_1, number_2, number_3)
min_num1 = min(number_1, number_2, number_3)

print(f"This is the bigest number: {max_num1}!")
print(f"This is the smallest number {min_num1}!")
