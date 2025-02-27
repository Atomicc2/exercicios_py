#Fazedno um sistema interativo do help

def ajuda(comando):
    print("Acessando o terminal de ajuda... ")
    help(comando)

while True:
    comando = str(input("Função ou biblioteca: "))
    if comando.upper() in 'FIM':
        break
    ajuda(comando)

print("FIM")
