#Criando um cicionário que retorna alguns parãmetros

def notas(*n, sit=False):
    x = {}
    x['total'] = len(n)
    x['maior'] = max(n)
    x['menor'] = min(n)
    x['media'] = sum(n) / len(n)
    if sit:
        if x['media'] >= 8:
            x['situação'] = "Boa"
        elif x['media'] >= 6:
            x['situação'] = "Média"
        else:
            x['situação'] = "Ruim"
    return x

print(notas(5, 7, 9, 3, 8, sit=True))