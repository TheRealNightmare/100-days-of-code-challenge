print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_string = name1 + name2

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t+r+u+e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l+o+v+e

score = int(str(true)+str(love))

if score < 10 or score > 90:
    print(f"your love score is {score}. You go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"your love score is {score}. You are alright together")
else:
    print(f"your love score is {score}")