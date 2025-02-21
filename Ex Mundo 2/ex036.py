#Aprovando empréstimo bancário
valor_casa = float(input("Qual o valor do imóvel? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos você pretende pagar? ")) * 12

prestação = valor_casa / anos
if prestação > 0.3 * salario:
    print("Infelismente seu impréstimo não foi liberado!")
    print(f"As parcelas ficaram em R${valor_casa / anos:.2f}, ou seja, maiorque 30% de R${salario}")
else:
    print(f"Parabéns, seu impréstimo foi liberado, o valor de cada parcela será de R${valor_casa / anos:.2f}")
