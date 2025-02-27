#Software que lê os dado do trabalhador e retorna alguns paramêtros

import datetime

data = {}

data['nome'] = str(input("Nome: "))
data['idade'] = datetime.datetime.now().year - int(input("Ano de nascimento: "))
data['ctps'] = int(input("Carteira de trabalho: [Digite 0 caso não tenha] "))

if data['ctps'] != 0:
    data['inicio'] = int(input("Ano de contratação: "))
    data['salario'] = float(input("Salário: "))
    data['aposento'] = (35 - (datetime.datetime.now().year - data['inicio'])) + data['idade']

for i, j in data.items():
    print(f"{i} = {j}")
