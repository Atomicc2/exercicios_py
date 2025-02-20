preço = float(input('Me fale o preço: '))
desconto = preço * 0.05
total = preço * 0.95
print('Para o valor de {:.1f}R$, o desconto é de {:.1f}, totalizando {:.1f}R$.'.format(preço, desconto, total))