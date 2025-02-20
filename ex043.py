#Fazendo o calculo do IMC

# Calculando o IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Você está com peso normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("Você está com obesidade grau 1.")
elif imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")
