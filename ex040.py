#Fazendo o calculo da média e retornado se está aprovado, recuperação ou reprovado

nota1 = float(input("Me fale sua primeira nota: "))
nota2 = float(input("Me fale sua segunda nota: "))

nota_final = (nota1 + nota2) / 2

if nota_final < 5:
    print(f"Reprovado, sua média foi {nota_final}")
elif nota_final >= 7:
    print(f"Você foi aprovado com média {nota_final}")
else:
    print(f"Você ficou de recuperação com média {nota_final}")