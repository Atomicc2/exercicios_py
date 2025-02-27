#Coleta dados de várias pessoas pessoas depois retorna alguns parâmetros

group = []
peaple = {}
sum_ages = 0

while True:
    
    peaple['name'] = str(input("Nome: "))
    
    while True:
        peaple['age'] = int(input("Idade: "))
        if not 1 < peaple['age'] < 120:
            print("Você não é um elfo, digite novamente a idade correta!")
        else:
            break
        
    sum_ages += peaple['age']
    
    while True:
        peaple['sex'] = str(input("Sexo: [M/F] ")).upper()
        if peaple['sex'] not in 'MF':
            print("ERRO! Digite apenas M ou F!")
        else: 
            break
    
    group.append(peaple.copy())
    peaple.clear()

    while True:
        choice = str(input("Deseja adicionar mais alguém? [S/N] ")).upper()
        if choice not in 'SN':
            print("ERRO! Digite apenas S ou N!")
        else: 
            break
    if choice in 'N':
        break

average = sum_ages / len(group)

print(f''' 
A) Você cadastrou um total de {len(group)} pessoas!
B) A média da idade é {average} anos
''')
print(f"C) A(s) mulhere(s) cadatrada(s) é/foram:", end=' ')
for i in group:
    if i['sex'] in 'Ff':
        print(f"{i['name']}")

print("Lista das pessoas que estão acima da média: ")

for i in group:
    if i['age'] > average:
        print(f"{'=>':>5} {i['name']} com {i['age']};")