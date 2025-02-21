#Pergunta qual o preço e a forma de pagamento e retorna o valor

valor = float(input("Informe o valor do pagamento: "))
print("Escolha a opção de pagamento abaixo: ")
print("Dinheiro/Cheque - 1\nA vista no cartão - 2\n2x no cartão - 3\n3x ou mais no cartão - 4")
pagamento = int(input("Digite o número correspondente: "))

if pagamento == 1:
    print(f"O valor a ser pago será de R${valor * 0.9:.2f}")
elif pagamento == 2:
    print(f"O valor a ser pago será de R${valor * 0.95:.2f}")
elif pagamento == 3:
    print(f"O valor a ser pago será o valor original!")
elif pagamento == 4:
    print(f"O valor a ser pago será de R${valor * 1.2:.2f}")