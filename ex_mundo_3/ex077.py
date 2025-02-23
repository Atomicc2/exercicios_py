#Fazendo uma lista das palavras e mostrano quais vogais tem

palavras = ('Anderson', 'Santos', 'Santana', 'Anelyse', 'Cristiana')

for item in palavras:
    print(f"\nNa palavra {item} temos ", end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    