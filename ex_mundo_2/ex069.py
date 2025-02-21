#Cadastra pessoas e depois exibe alguns parâmetros

mais_18 = 0
quantidade_homens = 0
mulheres_menos_20 = 0

while True:

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if sexo in 'M':
        quantidade_homens += 1

    idade = int(input("Idade: "))
    if idade >= 18:
        mais_18 += 1 

    if sexo in 'F' and idade < 20:
        mulheres_menos_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Quer adicionar algo mais? [S/N] ")).strip().upper()[0]
    if resposta in 'N':
        break

print("-----" * 8)
print(f'''Dessas pessoas:
{mais_18} são maiores de 18 anos!
{quantidade_homens} são homens!
{mulheres_menos_20} são mulheres com menos de 20 anos de idade!''')
print("-----" * 8)