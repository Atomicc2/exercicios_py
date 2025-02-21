#Refazendo o exercicio 35 porém acrescentando qual triangulo forma

print("Give-me three numbers: ")

a = float(input("1º: "))
b = float(input("2º: "))
c = float(input("3º: "))

if a + b > c and a + c > b and c + b > a:
    print("These three values can indeed form a triangle!")
    if a != b and b != c and a != c:
        print("triângulo escaleno!")
    elif (a != b and a == c) or (a == b and a != c):
        print("Esse triangulo é isóceles")
    else:
        print("Triângulo equilátero")
else:
    print("Thease three values not can form a triangle!")
