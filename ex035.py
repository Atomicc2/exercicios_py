print("Give-me three numbers: ")

a = float(input("1º: "))
b = float(input("2º: "))
c = float(input("3º: "))

if a + b > c and a + c > b and c + b > a:
    print("These three values can indeed form a triangle!")
else:
    print("Thease three values not can form a triangle!")