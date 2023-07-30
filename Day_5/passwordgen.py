import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print('''
  _____                                           _    _____                                 _               
 |  __ \                                         | |  / ____|                               | |              
 | |__) |__ _  ___  ___ __      __ ___   _ __  __| | | |  __   ___  _ __    ___  _ __  __ _ | |_  ___   _ __ 
 |  ___// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` | | | |_ | / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|
 | |   | (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| | | |__| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |   
 |_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|  \_____| \___||_| |_| \___||_|   \__,_| \__|\___/ |_|                                                                                                      
''')

nr_letters = int(input("How many letters would you like in your password?\n=>"))
nr_symbols = int(input("How many symbols would you like in your password?\n=>"))
nr_number = int(input("How many numbers would you like in your password?\n=>"))

password = []

for char in range(1,nr_letters+1):
    password.append(random.choice(letters)) 

for num in range(1,nr_number+1):
    password.append(random.choice(numbers))

for sym in range(1,nr_symbols+1):
    password.append(random.choice(symbols)) 

#shuffle() shuffles the items in the list 

random.shuffle(password)

p = ""

for x in password:
    p += x

print(f"you password is: {p}")

