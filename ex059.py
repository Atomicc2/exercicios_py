#Programa que lê dois valores e fala algumas opções de como prosseguir

resposta = 0
while resposta != 5:

    num1 = int(input("Me fale um número: "))
    num2 = int(input("Me fale outro número: "))

    resposta = int(input('''Me fale o que deseja fazer em seguida:
[ 1 ] - Somar
[ 2 ] - Multiplicar 
[ 3 ] - Saber qual o maior
[ 4 ] - Escolher outros números
[ 5 ] - Sair
Resposta: '''))
    
    if resposta == 1:
        print(f"A soma vale {num1 + num2}")

    if resposta == 2:
        print(f"A multiplicação vale {num1 * num2}")

    if resposta == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que o número {num2}")
        else:
            print(f"O número {num2} é maior que o número {num1}")

    if resposta == 4:
        print("Okay")

    if resposta == 5:
        print("Bye Bye...")