from math import sqrt, hypot

cateto_op = int(input('Qual o cateto oposto? '))
cateto_ad = int(input('Qual o cateto adjecente? '))

#result = sqrt(cateto_op ** 2 + cateto_ad ** 2)

result = hypot(cateto_ad, cateto_op)
print(f'A hipotenusa é {result:.0f}')

