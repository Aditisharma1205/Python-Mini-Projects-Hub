from turtle import Turtle, Screen
import random
is_race_on =False
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput("make your bet","which turtle will win the race enter your color ")
color=["red","purple","blue","green","yellow","pink"]
axis=[10,30,50,-10,-30,-50]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(-230, axis[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"you win, the {winning_color} turtle wins!")
            else:
                print(f"you lose, the {winning_color} turtle wins!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
