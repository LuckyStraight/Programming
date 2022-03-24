#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     clock face
#
# Filename:     3-4
# Date:  9/1/2021
#-------------------------------------------------------------------------------

#import class
import turtle

#setup of screen object and properties
wn = turtle.Screen()
wn.bgcolor("orange")

#setup turtle object and properties
chad = turtle.Turtle()
chad.shape("arrow")
chad.color("white")
chad.pensize(4)

#setup a for loop in range(30,361,30)
for i in range(30,361,30):
    chad.penup()
    chad.forward(50)
    chad.pendown()
    chad.forward(25)
    chad.penup()
    chad.forward(15)
    chad.stamp()
    chad.home()
    chad.left(i)

#draw lines in loop
wn.mainloop()