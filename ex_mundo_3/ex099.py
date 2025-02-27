#Função que lê vários valores e retorna o total de valores informados e o maior entre eles

def contador(* num):
    print("Analisando os valores informados...")
    for i in num:
        print(i, end=' ')
    print(f"Foram informados {len(num)} valores ao todo!")
    print(f"O maior deles é {max(num)}")

contador(1, 2, 3, 4, 5, 6, 7, 8, 9,)
