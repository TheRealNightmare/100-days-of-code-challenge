print("Welcome to nightmare pizza Deliveries!")
size =  input("What size do you want? {S, M, or L}").lower()
add_pepperoni = input("Do you want pepperoni? {Y or N}").lower()
extra_cheese = input("Do you want extra cheese? {Y or N}").lower()

price = 0

if size == "s":
    price+=15
elif size == "m":
    price+=20
else:
    price+=25

if add_pepperoni == "y":
    if size == "s":
        price+=2
    else:
        price+=3

if extra_cheese == "y":
     price+=1

print(f"your final price is ${price}")