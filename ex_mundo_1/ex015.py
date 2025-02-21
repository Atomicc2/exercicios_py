km = float(input('Quantos kilometros foram rodados? '))
dias = int(input('Por quantos dias? '))
preço = (dias * 60) + (km * 0.15)
print('O preço a ser pago será de {:.2f}'.format(preço))