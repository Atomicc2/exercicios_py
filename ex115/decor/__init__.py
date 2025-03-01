#Funções de estilização 

def linha():
    return "-" * 30

def cabecalho(msg):
    print(linha())
    print(msg.center(30))

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    cont = 1
    for i in lista:
        print(f"{cont} - {i}")
        cont += 1
    print(linha())