print("Welcome to the rollercoaster!")
height = int(input("height in cm: "))
bill = 0
if height>=120:
    print("You can ride the rollercoaster")

    age = int(input("age: "))
    if age<12:
        bill+=5
    elif age<=18:
        bill+=7
    else:
        bill+=12
    
    photo =  input("Do you want to take a photo? (y/n): ")
    if photo == "y":
        bill+=3
        
    print(f"Your bill is ${bill}")

else:
    print("You can't ride the rollercoaster")