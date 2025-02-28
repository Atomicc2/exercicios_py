#Funções input para o exercício 115

def input_int(msg):
    '''
    Use para pedir e válidar números inteiros (O nome é bem sujestivo!!!)
    '''
    while True:
        try:
            n = int(input(f"{msg }"))
        except (ValueError, TypeError, InterruptedError):
            print(f"\033[0,32,40mERRO!, Digite um número inteiro!\033[m")
        else:
            return n
        
def input_float(msg):
    '''
    Use para pedir e validar números float
    '''
    while True:    
        try:
            n = str(input(f"{msg} ")).replace(',', '.').strip()
            if n.isalpha():
                print("ERRO! Insira um valor válido!")
        except (ValueError, TypeError):
            print("ERRO! Insira um valor válido! ")
        else:
            return n
            