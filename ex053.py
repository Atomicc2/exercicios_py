#Fazendo um detector de palíndromo

palavra = str(input("Me fale a palavra: ")).strip().lower()

separa = palavra.split()
junta = ''.join(separa)
contrario = junta[::-1]
if junta == contrario:
    print(f"A palavra {palavra} fica {contrario} ao contrário, ou sejá, é um palíndromo!")
else:
    print(f"A palavra {palavra} fica {contrario} ao contrário, ou seja, não é um palindomo!")