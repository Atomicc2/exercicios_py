#Fazendo uma sequência de fiboncci

num = int(input("Me fale um número: "))

contagem = 3
t1 = 0
t2 = 1
t3 = 0

print("-=-" * num)
print(f"{t1} - ", end='')
print(f"{t2} - ", end='')

while contagem <= num:
    t3 = t1 + t2
    print(t3, end=' - ')
    t1 = t2
    t2 = t3
    contagem += 1

