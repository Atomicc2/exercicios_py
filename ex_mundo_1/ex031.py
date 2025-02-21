km = float(input("Tell me how many kms you traveled: "))
price = km * 0.5 if km <= 200 else km * 0.45

#if km <= 200:
#    print(f"The ticket sill cost R${km * 0.50}")
#else:
print(f"This ticket will cost R${price:.2f}")

