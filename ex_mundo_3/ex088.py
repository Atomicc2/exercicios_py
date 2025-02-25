#Gerando 6 números aleatórios para a mega cena (de 0 a 100) quants vezes quiser

import random, time

resposta = int(input("Quantos sequências da mega sena quer gerar? "))

for i in range(0, resposta):
    n = random.sample(range(1, 101), k=6)
    print(n)    
    time.sleep(0.5)