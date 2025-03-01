from ex115.input import *
from ex115.decor import *
from ex115.arq import *

#main

nome_arquivo = 'cadastros.txt'
if not arquivo_existe(nome_arquivo):
    criar_arquivo(nome_arquivo)

lista = []
while True:
    
    cabecalho("LISTA DE CADASTROS")
    menu(['Novo cadastro', 'Listar cadastros', 'Sair'])
    escolha = input_int("Digite a opção desejada: ")

    if escolha == 1:
        cabecalho("NOVO CADASTRO")
        nome = input_str("Nome: ")
        idade = input_int("Idade: ")
        cadastrar(nome_arquivo, nome, idade)

    elif escolha == 2:
        print(linha())
        ler_arquivo(nome_arquivo)
        
    elif escolha == 3:
        cabecalho('Até logo')
        print(linha())
        break

    else:
        print("ERRO!, Digite uma opção válida!")