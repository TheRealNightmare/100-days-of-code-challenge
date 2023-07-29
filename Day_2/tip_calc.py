print("Welcome to the tip calculator")

bill = float(input("Toltal Bill $"))
tip =  int(input("How much tip would you like to give (in %)?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = bill + (bill*tip/100)
split_bill = bill_with_tip/people

print(f"Each People should pay ${split_bill}")