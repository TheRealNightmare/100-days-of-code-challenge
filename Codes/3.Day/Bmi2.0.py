height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = round(weight/height**2)

if bmi<18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi<35:
    print(f"Your bmi is {bmi}, you are abese")
else:
    print(f"Your bmi is {bmi}, you are clinicaly obese")
