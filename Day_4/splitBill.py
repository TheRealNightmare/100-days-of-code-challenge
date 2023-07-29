import random

name = input("Give me everybody's names, seperated by a comma.").split(',')

rand = random.randint(0, (len(name)-1))
print(f"The person who is gonna give bill: {name[rand]}")