import random

p1 = str(input("What's a first person? "))
p2 = str(input("What's a second person? "))
p3 = str(input("What's a third person? "))
p4 = str(input("What's a fourth person? "))
p5 = str(input("What's a fifth person? "))

list = [p1, p2, p3, p4, p5]

rand = random.choice(list)
print(rand)