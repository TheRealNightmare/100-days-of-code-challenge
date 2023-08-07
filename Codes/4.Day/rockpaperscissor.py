import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock,paper,scissor]

user= int(input("What do you choose?\n0 for rock\n1 for paper\n2 for scissor\n"))
if user>=3 or user<0:
    print("Invalid!")
else:
    print(image[user])

    computer = random.randint(0,2)
    print("Computer chose: ")
    print(image[computer])

    if user == 0  and computer == 2:
        print("You Win!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You Lose!")
    elif user > computer:
        print("You Win!")
    elif user == computer:
        print("Draw")