#Confere seu alistamento militar

idade = int(input("Me fale a sua idade: "))

if idade < 18:
    print(f"Você precisará se alistar daqui a {idade - 18} anos!")
elif idade == 18:
    print(f"Você já está na idade de fazer o alistamento")
else:
    print(f"Você já passou da idade de se alistar fazem {idade - 18} anos!")