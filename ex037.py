#Conretendo numeros em outras bases

number = int(input("Me fale um número qualquer: "))

binario = bin(number)
octal = oct(number)
hexadecimal = hex(number)

print(f"Binário: {binario[2:]}\nOctal: {octal[2:]}\nHexadecimal {hexadecimal[2:]}")