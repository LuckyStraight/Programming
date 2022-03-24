#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sammy's Logo
#
# Filename:     3-5
# Date:  9/1/2021
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

wn.mainloop()