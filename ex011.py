largura_parede = float(input('Me fale a largura da parede: '))
comprimento_parede = float(input('Me fale agora o comprimento dela: '))
area_parede = largura_parede * comprimento_parede
tinta_parede = area_parede // 2 + 1
print('Como a área total da parede é {:.2f} m2, você vai precisar de {:.0f} baldes de tinta para pinta-la por completo'.format(area_parede, tinta_parede))