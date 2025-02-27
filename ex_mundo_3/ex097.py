#criando uma função ptint melhorada

def printf(txt):
    x = len(txt)
    print("-" * (x + 4))
    print(f"  {txt}")
    print("-" * (x + 4))

msg = str(input("Digite a mensagem a ser formatada: "))
printf(msg)