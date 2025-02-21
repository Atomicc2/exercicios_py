#Criando umbot pra jogar par ou impar até perder

from random import randint

num = 0
escolha = ''
random = 0
resultado = 0
par_ou_impar = ''
contagem = 0

while True:

    escolha = str(input("Você escolhe Par ou Impar? [P/I] ")).upper()
    num = int(input("Digite um número: "))
    random = randint(0, 11)
    resultado = (num + random) % 2

    if resultado == 0:
        par_ou_impar = 'Par'
    else:
        par_ou_impar = 'Impar'

    if (resultado == 0 and escolha in 'P') or (resultado == 1 and escolha in 'I'):
        print("-=-" * 20)
        print(f"Parabéns, você ganhou!!")
        print(f"Eu escolhi {random}, somando com {num} da {random + num} que é um número {par_ou_impar}")
        print("-=-" * 20)
        contagem += 1
    else:
        print(f"Que pena, você perdeu, a soma dos números deu {num + random} que é {par_ou_impar}")
        break
if contagem > 1:
    print(f"Você ganhou {contagem} vezes consecutivas!!")
elif contagem == 1:
    print("Você ganhou apenas uma vez!")