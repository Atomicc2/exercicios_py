#Fazendo uma lista de produtos e valores

lista = ('Pão', 3, 'Café', 5, 'Açucar', 8)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:-<15}", end='')
    else:
        print(f"R${lista[i]:>6.2f}")
    