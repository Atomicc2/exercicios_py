#Pede que insira um expressão e diz se os parênteses estão de forma correta

expressao = list(input("Digite a expressão: "))
parentese_1 = parentese_2 = 0
           
for i  in expressao:
    if i in '(':
        parentese_1 += 1
    elif i in ')':
        parentese_2 += 1

if parentese_1 == parentese_2:
    print("A expressão está correta!!")
else:
    print("A expressão está errada!!")