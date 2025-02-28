def leia_int(msg):
    while True:
        try:
            entrada = int(input(f"{msg}"))
        except ValueError:
            print(f"ERRO! Insira um caractére válido!")
        else: 
            break
    return entrada

def leiafloat(msg):
    while True:
        try:
            entry = float(input(f"{msg}"))
        except ValueError:
            print(f"Tente novmamente!")
        else:
            break
    return entry
            

