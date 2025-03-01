from ex115.input import * 
from ex115.decor import *

#main

lista = []
while True:
    
    cabecalho("LISTA DE CADASTROS")
    menu(['Novo cadastro', 'Listar cadastros', 'Sair'])
    escolha = input_int("Digite a opção desejada: ")

    if escolha == 1:
        i = {}
        i['nome'] = input_str("Nome: ")
        i['idade'] = input_int("Idade: ")
        lista.append(i.copy())
        i.clear()
        
    if escolha == 2:
        print(linha())
        print(lista)

    if escolha == 3:
        cabecalho('Até logo')
        break