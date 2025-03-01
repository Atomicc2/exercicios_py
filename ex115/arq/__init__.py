#Funções para manipulaçõa de arquivos

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um problema na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado!")
        return(nome)

def ler_arquivo(nome):
    try: 
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        print(a.read())
    finally:
        a.close()

def cadastrar(arquivo, nome, idade):
    try: 
        a = open(arquivo, 'at')
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome:<20}{idade} Anos\n")
        except:
            print("Houve um erro ao adicionar um novo cadastro!")
        else:
            print(f"{nome} cadastrado!")
            a.close()
