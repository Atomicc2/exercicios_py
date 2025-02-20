#Lê o nome, idade e sexo e retorna alguns parâmetros

totmedia = 0
velho = ''
idadevelho = 0
mulher20 = 0

for i in range(1, 5):
    print(f"-=-= {i}ª Pessoa =-=-=-")
    nome = str(input("Fale sua nome: "))
    idade = int(input("Fale sua idade: "))
    sexo = str(input("Fale seu sexo [M/F]: "))
    totmedia += idade
    if sexo in 'Mm' and idade >= idadevelho:
        idadevelho = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media = totmedia / 4

print(f"A média das idades é {media}!")
print(f"O homem mais velho é {velho}!")
print(f"{mulher20} mulher(es) tem menos de 20 anos!")