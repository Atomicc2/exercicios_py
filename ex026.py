name = str(input("Say a pharse: ")).strip()


print(f"The letter 'A' appears {name.upper().count("A")} times!")
print(f"The firt letter 'A' appears in location {name.upper().find('A')}")
print(f"The last letter 'A' appears ind location {name.upper().rfind('A')}")
