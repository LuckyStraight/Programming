#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Turtles in a while loop
#
# Filename:     7-4
# Date:  10/6/2021
#--------------------------------------------------------------------------------

import turtle
import random

bhavani = turtle.Turtle()
bhavani.color("magenta")
bhavani.shape("turtle")
bhavani.pensize(5)
bhavani.speed(5)

karin = turtle.Turtle()
karin.color("blue")
karin.shape("arrow")
karin.pensize(5)
karin.speed(5)

wn = turtle.Screen()
wn.bgcolor("black")

def isInScreen(wn,t,t2):
    xmin = -wn.window_width() / 2
    xmax = wn.window_width() / 2
    ymin = -wn.window_height() / 2
    ymax = wn.window_height() / 2

    words = ["Kaboom!", "Shazam!", "Pow!", "Wham!", "Boom!", "Zap!"]
    rng = random.randrange(6)

    x = t.xcor()
    y = t.ycor()

    if x < xmin or x > xmax:
        return False
    if y < ymin or y > ymax :
        return False

    x2 = t2.xcor()
    y2 = t2.ycor()

    if x2 < xmin or x2 > xmax:
        return False
    if y2 < ymin or y2 > ymax :
        return False
    if x == x2:
        t.write(words[rng])
    return True

def main():
    while isInScreen(wn,bhavani,karin):
        bhavani.fd(50)
        karin.fd(50)
        coin = random.randrange(2)
        if coin == 0:
            bhavani.left(90)
        else:
            bhavani.right(90)
        coin = random.randrange(2)
        if coin == 0:
            karin.left(90)
        else:
            karin.right(90)



    turtle.mainloop()

main()
