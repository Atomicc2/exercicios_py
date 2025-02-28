def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(f"{msg}")).replace(',', '.').strip()
        if entrada.isalpha():
            print("ERRO! Entrada inválida!")
        else:
            valido = True
            return float(entrada)