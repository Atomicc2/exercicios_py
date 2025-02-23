#pedindo ao usuário um número entro 0 e 20 e retornando o nome do valor po extenso

numbers_in_full = (
    "Zero", "One", "Two", "Three", "Fuor", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fuorteen", "Fifteen",
    "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"
)

number = -1
while not 0 <= number <= 20:
    number = int(input("Me fale um número entre 0 e 20: "))

print(f"You entered the number {numbers_in_full[number]}")
