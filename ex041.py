#Seletor de categoria de acordo com a idade

idade = int(input("Digite a sua idade: "))

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

print(f"Sua categoria é: {categoria}")