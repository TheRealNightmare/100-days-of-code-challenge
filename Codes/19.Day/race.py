from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

y = [-70, -40, -10, 20, 50, 80]
color= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y[i])
    all_turtles.append(new_turtle)
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You have Won. The {winning_color} turtle won")
            else:
                print(f"You have lostThe {winning_color} turtle won")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()