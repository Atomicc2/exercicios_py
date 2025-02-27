#Criando uma função que retorna se o voto é obrigatório ou não 

import datetime

def voto(a=0):
    idade = datetime.datetime.now().year - a
    if idade < 16:
        print(f"Com {idade} anos você ainda não pode votar!")
    elif 16 <= idade <= 17 or idade > 65:
        print(f"Com {idade} anos você pode votar, mas não é obrigatório!")
    else:
        print(f"Com {idade} anos é obrigatório votar!")

ano = int(input("Em que ano você nasceu? "))
voto(ano)