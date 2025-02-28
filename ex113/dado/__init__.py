def leia_int(msg):
    while True:
        try:
            entrada = int(input(f"{msg}"))
        except (ValueError, TypeError):
            print(f"ERRO! Insira um caractére válido!")
            continue
        else: 
            break
    return entrada

def leiafloat(msg):
    while True:
        try:
            entry = float(input(f"{msg}"))
        except (ValueError, TypeError):
            print(f"ERRO! Insira um caractére válido!")
            continue
        else:
            break
    return entry
            

