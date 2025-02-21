#Fazendo um programa que lê o valor e retorna a quantidae de cada cédula ele receberá

valor = int(input("Me fale o valor: "))
total = valor
cedula = 50
tot_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        tot_cedula += 1
    else:
        if tot_cedula > 0:
            print(f"Você receberá {tot_cedula} de cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        tot_cedula = 0

        if total == 0:
            break



