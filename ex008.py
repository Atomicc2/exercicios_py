numero = float(input('Me diga o número a qual deseja converter(em metros): '))
decimetros = numero * 10
centimetros = numero * 100
milimetros = numero * 1000
print('Decímetros: {:.1f}\nCentímetros: {:.1f}\nMilímetros: {:.12f}'.format(decimetros, centimetros, milimetros))
