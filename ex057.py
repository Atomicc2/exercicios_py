#Requisitano o sexo até inserir o correto
sexo = str(input("Me informe seu sexo [M/F]: ")).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input("Opção inválida, tente novamente: ")).upper().strip()[0]

if sexo == 'M':
    print("Você é do sexo masculino")
else:
    print("Você é do sexo feminino!")