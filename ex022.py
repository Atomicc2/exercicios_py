name = str(input("What's your name complet? ")).strip()
name_list = name.split()
name_list_board = "".join(name_list)

print(f"This is a upper name: {name.upper()}!")
print(f"This is a lower name: {name.lower()}!")
print(f"This is a firt name: {name_list[0]}!")
print(f"This is the amount of letters: {len(name_list_board)}!")
