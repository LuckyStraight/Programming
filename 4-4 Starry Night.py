#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     starry night
#
# Filename:     4-4
# Date:  9/7/2021
#-------------------------------------------------------------------------------

# import statements
import turtle
from random import randint

def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.setup(600,600)
    chad = turtle.Turtle()
    chad.color("yellow")
    chad.speed(0)
    manystars(chad)
    chad.hideturtle()

#the code to draw a single star
def drawstars(t):
    turns = 5
    t.begin_fill()
    while turns > 0:
        t.forward(50)
        t.left(145)
        turns = turns - 1
    t.end_fill()

#code to draw 50 stars
def manystars(t):
    for i in range(50):
        x = randint(-250, 250) #random x-coordinate
        y = randint(-250, 250) #random y-coordinate
        drawstars(t)
        t.penup()
        t.goto(x,y)
        t.pendown()

main()

wn.mainloop()