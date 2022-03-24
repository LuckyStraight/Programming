#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sammy's Logo
#
# Filename:     10-3
# Date:  10/28/2021
#-------------------------------------------------------------------------------


import turtle

wn = turtle.Screen()
wn.bgcolor("orange")
wn.title("Sammy's Logo")

mike = turtle.Turtle()
mike.shape("circle")
mike.color("yellow")
mike.speed(10)
turtle.setup(800,800)

mike.penup()
size =  5
for i in range(70):
    mike.stamp()
    size = size + 1
    mike.forward(size)
    mike.right(45)


chad = turtle.Turtle()
chad.shape("arrow")
chad.color("yellow")
chad.pensize(4)
chad.speed(10)

def red():
    wn.bgcolor("red") #changes the background to red

def green():
    wn.bgcolor("green") #changes the background to green

def blue(x,y):
    if "blue" != wn.bgcolor(): #changes the color to blue if background isn't equal to blue
        wn.bgcolor("blue")
    else:
        wn.bgcolor("orange")

def orange(x,y):
    wn.bgcolor("orange") #allows the background to switch from blue to orange

for i in range(30,361,30):
    chad.penup()
    chad.forward(180)
    chad.pendown()
    chad.forward(30)
    chad.penup()
    chad.forward(40)
    chad.stamp()
    chad.backward(250)
    chad.left(360/12)

bill = turtle.Turtle()
bill.color("maroon")
bill.write("Sammy's Seashore Supplies", align = "center", font = ("Papyrus",24,"bold"))
bill.hideturtle()

wn.onkey(red, "r")
wn.onkey(green, "g")


wn.onclick(blue)

wn.listen()
wn.mainloop()