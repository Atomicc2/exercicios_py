salary = float(input("Say the you salary: "))
satifaction = float(input("Give your satisfaction rate: "))

if salary > 1200 and satifaction > 6:
    print(f"From now on your salary will be: R${salary * 1.10:.2f}, congratulations!!!")
elif satifaction >= 6:
    print(f"From now on your salary wil be: R${salary * 1.15:.2f}, congratulations!!!")
else:
    print(f"Satisfaction {satifaction:.1f} is very low. It will not be possible to increase the salary")
