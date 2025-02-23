#Criando uma tupla com os 20 primeiros colocados do brasileirão e retonando algumas informações

clubes_brasileirao_2025 = (
    "Atlético-MG", "Bahia", "Botafogo", "Bragantino", "Ceará", "Corinthians",
    "Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional",
    "Juventude", "Mirassol", "Palmeiras", "Santos", "Sport", "São Paulo",
    "Vasco", "Vitória"
)
print("-" * 40)
print("Lista dos primeiros 20 colocados:")
print(f"{clubes_brasileirao_2025}")
print("-" * 40)
print(f"Os primeiros 5 colocados são: {clubes_brasileirao_2025[:6]}")
print("-" * 40)
print(f"Os 4 últimos são: {clubes_brasileirao_2025[-4:]}")
print("-" * 40)
print(f"O time do {clubes_brasileirao_2025[7]} está na 8ª posição")
print("-" * 40)
print(f"Em ordem alfabética fica: {sorted(clubes_brasileirao_2025)}")
print("-" * 40)